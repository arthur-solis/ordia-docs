# Contratos REST do MVP

Catálogo inicial de endpoints do MVP. É uma definição de contrato para orientar OpenAPI e implementação; não representa endpoints já disponíveis.

## Convenções

- Base: `/api/v1`
- Endpoints protegidos exigem `Authorization: Bearer <access-token>`.
- Tenant Context vem do token validado no backend.
- IDs enviados pelo cliente nunca substituem validação de Tenant, Membership e permission.
- Formato de erro segue [padrão da API](README.md#9-erros).
- Listagens usam `page` e `pageSize`, com limite de `100`.

## Identity & sessão

| Método e rota | Permission | Resultado |
|---|---|---|
| `POST /auth/login` | pública | Credenciais válidas retornam access e refresh token. |
| `POST /auth/refresh` | refresh válido | Rotaciona tokens. |
| `POST /auth/logout` | autenticado | Invalida refresh token atual. |
| `POST /auth/password-recovery` | pública | Resposta não enumerável. |
| `POST /auth/password-reset` | token de recuperação | Redefine senha e invalida sessões de renovação. |
| `POST /auth/switch-tenant` | Membership ativa no destino | Emite novo par de tokens no Tenant escolhido. |

## Tenant e Memberships

| Método e rota | Permission | Resultado |
|---|---|---|
| `POST /tenants` | fluxo de criação | Cria Tenant e administrador inicial. |
| `GET /tenants/current` | `tenant:read` | Retorna Tenant Context atual. |
| `PATCH /tenants/current` | `tenant:update` | Atualiza dados permitidos. |
| `GET /memberships` | `tenant:manage_members` | Lista Memberships do Tenant atual. |
| `POST /memberships/invitations` | `tenant:manage_members` | Cria convite e Membership `PENDING`. |
| `PATCH /memberships/{id}` | `tenant:manage_members` ou `tenant:manage_roles` | Altera estado ou roles, respeitando proteção do último admin. |

## Patients

| Método e rota | Permission | Resultado |
|---|---|---|
| `GET /patients` | `patient:read` | Busca paginada no Tenant atual. |
| `POST /patients` | `patient:create` | Cria Patient e retorna alerta de possível duplicidade quando houver. |
| `GET /patients/{id}` | `patient:read` | Retorna Patient autorizado. |
| `PATCH /patients/{id}` | `patient:update` | Atualiza dados permitidos. |
| `POST /patients/{id}/archive` | `patient:archive` | Arquiva Patient. |
| `POST /patients/{id}/reactivate` | `patient:update` | Reativa Patient. |

## Recursos e Agenda

| Método e rota | Permission | Resultado |
|---|---|---|
| `GET /resources` | `resource:read` | Lista Resources do Tenant atual. |
| `POST /resources` | `resource:manage` | Cria Resource. |
| `PATCH /resources/{id}` | `resource:manage` | Atualiza Resource ou disponibilidade. |
| `POST /resources/{id}/deactivate` | `resource:manage` | Desativa após resolver Appointments futuros. |
| `GET /appointments` | `appointment:read` | Agenda filtrada por período e recurso. |
| `POST /appointments` | `appointment:create` | Cria Appointment ou retorna `409` em conflito. |
| `GET /appointments/{id}` | `appointment:read` | Retorna Appointment autorizado. |
| `PATCH /appointments/{id}` | `appointment:update` | Altera dados e revalida conflito. |
| `POST /appointments/{id}/confirm` | `appointment:confirm` | Confirma Appointment. |
| `POST /appointments/{id}/cancel` | `appointment:cancel` | Cancela e libera recursos. |
| `POST /appointments/{id}/complete` | `appointment:complete` | Conclui Appointment. |
| `POST /appointments/{id}/no-show` | `appointment:mark_no_show` | Registra ausência. |

## Arquivos, relatórios e auditoria

| Método e rota | Permission | Resultado |
|---|---|---|
| `POST /files` | `file:upload` | Solicita upload para recurso proprietário permitido. |
| `GET /files/{id}/download` | `file:read` | Entrega autorizada ou URL assinada de curta duração. |
| `DELETE /files/{id}` | `file:remove` | Executa remoção lógica. |
| `GET /reports/{type}` | `report:read` | Retorna relatório autorizado. |
| `POST /exports` | `report:export` | Cria job de exportação. |
| `GET /exports/{id}` | `report:export` | Consulta estado e resultado autorizado. |
| `GET /audit-events` | `audit:read` | Lista eventos autorizados. |

## Status específicos

| Situação | HTTP |
|---|---:|
| Credencial ausente, inválida ou expirada | 401 |
| Membership, Tenant ou permission insuficiente | 403 |
| Recurso fora do Tenant/escopo ou inexistente | 404 |
| Conflito de agenda, transição ou último administrador | 409 |
| Validação de entrada | 400 ou 422 |
| Limite de login, recuperação ou exportação | 429 |

## Contrato verificável

O [OpenAPI inicial](openapi-mvp.yaml) já materializa os fluxos prioritários com schemas e erros. Na Fase 3, ele deve crescer junto dos endpoints reais e alimentar testes de contrato.
