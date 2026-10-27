# Estratégia de Migrations do MVP

Nenhuma alteração de banco em produção será manual. A implementação da Fase 3 deverá usar **Flyway** com migrations SQL imutáveis, aplicadas automaticamente no pipeline controlado.

## Convenções

- Local: `backend/src/main/resources/db/migration`.
- Nome: `VNNN__descricao_em_snake_case.sql`.
- Uma migration publicada não é alterada: a correção é uma nova migration.
- Cada migration deve ser testada em banco vazio e como upgrade do último schema liberado.
- Dados de referência (roles e permissions) devem ser idempotentes e versionados junto ao schema.
- Operações destrutivas exigem ADR, backup verificado e plano de reversão.

## Plano inicial

| Migration | Conteúdo | Verificações mínimas |
|---|---|---|
| `V001__create_tenants_and_users.sql` | `tenants`, `users`, auditoria básica e convenções de data/UUID. | criação de Tenant e isolamento de usuários. |
| `V002__create_memberships_rbac_and_sessions.sql` | Memberships, roles, permissions, associações, convites, refresh e recuperação. | último administrador, rotação/revogação, convite. |
| `V003__create_patients.sql` | Pacientes, índices de busca e arquivamento lógico. | escopo por Tenant e alerta de duplicidade. |
| `V004__create_resources_and_appointments.sql` | Recursos, disponibilidade, bloqueios, agenda e associações. | conflito concorrente e transições válidas. |
| `V005__create_files_exports_and_audit.sql` | Metadados de arquivo, exportações e eventos de auditoria. | autorização, expiração e imutabilidade operacional. |

## Evolução segura

1. Preferir alterações aditivas e compatíveis.
2. Para remover coluna ou contrato, usar expandir → migrar dados → trocar aplicação → remover em versão posterior.
3. Alterações de índice devem ser avaliadas para tamanho de tabela e janela operacional.
4. Toda migration que movimentar dados deve registrar volume esperado, tempo estimado e estratégia de retomada.
5. Backups e restauração devem ser validados conforme [Privacidade e LGPD operacional](../security/privacy-mvp.md).

## Fora desta etapa

Estes arquivos são um plano técnico. As migrations SQL, a configuração do Flyway e os testes automatizados só serão criados quando a Fase 3 for autorizada.
