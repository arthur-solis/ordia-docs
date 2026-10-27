# Modelo Físico Inicial do MVP

Este documento transforma o [modelo de domínio](../product/domain-model.md) em uma referência de persistência para o MVP. Ele define a intenção do schema; não é ainda uma migration executável nem autoriza o início da Fase 3.

## Convenções

- Banco: MySQL 8.0+, charset `utf8mb4`, collation `utf8mb4_0900_ai_ci`.
- Chaves primárias: `BINARY(16)`, com UUIDv7 gerado pela aplicação. A API serializa IDs como UUID textual.
- Datas: `DATETIME(6)` em UTC. A timezone de apresentação pertence ao Tenant.
- Estados e tipos: `VARCHAR(32)` com validação na aplicação e `CHECK` quando a versão/configuração do MySQL permitir.
- Dados de Tenant: toda tabela tenant-scoped recebe `tenant_id NOT NULL`; consultas e índices começam por esse campo.
- Exclusão lógica: usar `archived_at`, `deactivated_at` ou `removed_at` conforme o domínio. Não usar exclusão física como operação normal do MVP.
- Senhas, tokens de refresh, recuperação e convite: persistir somente hashes, nunca o segredo original.

## Tabelas e relacionamentos

| Tabela | Campos essenciais | Integridade e índices |
|---|---|---|
| `tenants` | `id, name, timezone, status, created_at, updated_at` | `status ∈ PENDING/ACTIVE/SUSPENDED/CLOSED`; índice `(status)`. |
| `users` | `id, full_name, email_normalized, password_hash, status, last_login_at, created_at, updated_at` | `UNIQUE(email_normalized)`; `status ∈ ACTIVE/DISABLED`. |
| `memberships` | `id, tenant_id, user_id, status, invited_at, activated_at, suspended_at, revoked_at, created_at, updated_at` | `UNIQUE(tenant_id, user_id)`; FKs para Tenant e User; índice `(tenant_id, status)`. |
| `roles` | `id, code, name, mvp_managed` | `UNIQUE(code)`; catálogo sem Tenant no MVP. |
| `permissions` | `id, code, description` | `UNIQUE(code)`; catálogo sem Tenant no MVP. |
| `role_permissions` | `role_id, permission_id` | PK composta; FKs. |
| `membership_roles` | `membership_id, role_id` | PK composta; FKs. Proteção do último `TENANT_ADMIN` é regra transacional da aplicação. |
| `refresh_token_sessions` | `id, user_id, token_hash, family_id, issued_at, expires_at, revoked_at, replaced_by_id, ip_hash, user_agent` | `UNIQUE(token_hash)`; índice `(user_id, expires_at)`; rotação por família. |
| `password_recovery_tokens` | `id, user_id, token_hash, expires_at, consumed_at, created_at` | `UNIQUE(token_hash)`; somente um token ativo por usuário. |
| `membership_invitations` | `id, membership_id, email_normalized, token_hash, expires_at, accepted_at, cancelled_at, created_by` | `UNIQUE(token_hash)`; convite é inseparável da Membership `PENDING`. |
| `patients` | `id, tenant_id, full_name, full_name_normalized, birth_date, document_normalized, phone, email_normalized, status, archived_at, created_by, updated_by, created_at, updated_at` | `status ∈ ACTIVE/ARCHIVED`; índices `(tenant_id, status, full_name_normalized)`, `(tenant_id, document_normalized)`, `(tenant_id, birth_date, full_name_normalized)`. Documento único apenas quando preenchido. |
| `resources` | `id, tenant_id, type, name, status, capacity, deactivated_at, created_at, updated_at` | `type ∈ PROFESSIONAL/ROOM/EQUIPMENT`; capacidade 1 no MVP; `UNIQUE(tenant_id, type, name)`. |
| `resource_schedules` | `id, tenant_id, resource_id, weekday, starts_at_local, ends_at_local` | índice `(tenant_id, resource_id, weekday)`. |
| `resource_blocks` | `id, tenant_id, resource_id, starts_at, ends_at, reason, created_by` | índice `(tenant_id, resource_id, starts_at, ends_at)`; intervalo `start < end`. |
| `appointments` | `id, tenant_id, patient_id, starts_at, ends_at, status, notes, cancelled_at, created_by, updated_by, created_at, updated_at` | índices `(tenant_id, starts_at)`, `(tenant_id, patient_id, starts_at)`; intervalo `start < end`. |
| `appointment_resources` | `appointment_id, resource_id` | PK composta; cada Appointment deve ter ao menos um recurso PROFESSIONAL ativo, validado na transação. |
| `files` | `id, tenant_id, owner_type, owner_id, object_key, original_name, content_type, byte_size, checksum, removed_at, created_by, created_at` | `UNIQUE(object_key)`; índice `(tenant_id, owner_type, owner_id)`. Dono polimórfico é validado pela aplicação. |
| `exports` | `id, tenant_id, requested_by, type, parameters_json, status, file_id, expires_at, created_at, completed_at, error_code` | índices `(tenant_id, status, created_at)`, `(requested_by, created_at)`. |
| `audit_events` | `id, tenant_id NULL, actor_user_id NULL, action, resource_type, resource_id, occurred_at, correlation_id, ip_hash, metadata_json` | somente inserção pela aplicação; índices `(tenant_id, occurred_at)`, `(tenant_id, action, occurred_at)`, `(correlation_id)`. |

## Regras de banco importantes

- FKs devem existir onde o relacionamento não é polimórfico e devem impedir referências órfãs.
- `tenant_id` não é inferido de um ID recebido pelo cliente. A aplicação compara o contexto autenticado e filtra toda leitura/escrita.
- MySQL não possui constraint de exclusão para intervalos. Conflitos de Agenda serão prevenidos por uma transação que bloqueia os recursos envolvidos e reconsulta Appointments/Blocks ativos antes de gravar.
- `audit_events` e os hashes de tokens não devem ser atualizados por fluxos de negócio comuns.
- A versão inicial não cria tabelas para Financeiro, Notificações ou Integrações, pois estão fora do MVP.

## Rastreabilidade

| Referência funcional | Materialização |
|---|---|
| Identity, Membership e RBAC | `users`, `memberships`, `roles`, `permissions` e suas tabelas de associação |
| Tenant Context | `tenant_id` nas entidades tenant-scoped e validação em servidor |
| Paciente e duplicidade | `patients` e seus índices de busca |
| Recursos e Agenda | `resources`, horários/bloqueios, `appointments`, `appointment_resources` |
| Arquivos e exportações | `files`, `exports` e armazenamento de objeto privado |
| Auditoria | `audit_events` |

## Próximos passos de implementação

A [estratégia de migrations](migrations.md) define a ordem de entrega do schema. Ao iniciar a Fase 3, cada migration deverá ser acompanhada de testes de isolamento de Tenant, integridade e concorrência de Agenda.
