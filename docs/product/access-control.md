# Matriz de Acesso do MVP

Catálogo inicial de permissões do ORDIA e composição das roles do MVP. Permissões são avaliadas no backend, sempre no Tenant Context e com Membership `ACTIVE`.

## 1. Convenções

- Permissão segue o formato `domínio:ação`.
- A ausência da permissão significa negação.
- `TENANT_ADMIN` administra o próprio Tenant, mas não possui acesso transversal implícito.
- `PLATFORM_ADMIN` não integra o MVP; qualquer capacidade transversal exige escopo e finalidade explícitos.
- Roles podem evoluir, mas a alteração deve manter rastreabilidade e testes de autorização.

## 2. Catálogo de permissões

| Domínio | Permissões do MVP |
|---|---|
| Tenant | `tenant:read`, `tenant:update`, `tenant:manage_members`, `tenant:manage_roles` |
| Pacientes | `patient:read`, `patient:create`, `patient:update`, `patient:archive` |
| Recursos | `resource:read`, `resource:manage` |
| Agenda | `appointment:read`, `appointment:create`, `appointment:update`, `appointment:confirm`, `appointment:cancel`, `appointment:complete`, `appointment:mark_no_show` |
| Arquivos | `file:read`, `file:upload`, `file:remove` |
| Relatórios | `report:read`, `report:export` |
| Auditoria | `audit:read` |

## 3. Matriz por role

| Permissão | Tenant Admin | Manager | Professional | Reception | Finance | Auditor |
|---|---:|---:|---:|---:|---:|---:|
| `tenant:read` | ✓ | ✓ |  |  |  |  |
| `tenant:update` | ✓ |  |  |  |  |  |
| `tenant:manage_members` | ✓ |  |  |  |  |  |
| `tenant:manage_roles` | ✓ |  |  |  |  |  |
| `patient:read` | ✓ | ✓ | ✓ | ✓ |  | ✓ |
| `patient:create` | ✓ | ✓ | ✓ | ✓ |  |  |
| `patient:update` | ✓ | ✓ | ✓ | ✓ |  |  |
| `patient:archive` | ✓ | ✓ |  |  |  |  |
| `resource:read` | ✓ | ✓ | ✓ | ✓ |  |  |
| `resource:manage` | ✓ | ✓ |  |  |  |  |
| `appointment:read` | ✓ | ✓ | ✓ | ✓ |  | ✓ |
| `appointment:create` | ✓ | ✓ | ✓ | ✓ |  |  |
| `appointment:update` | ✓ | ✓ | ✓ | ✓ |  |  |
| `appointment:confirm` | ✓ | ✓ | ✓ | ✓ |  |  |
| `appointment:cancel` | ✓ | ✓ | ✓ | ✓ |  |  |
| `appointment:complete` | ✓ | ✓ | ✓ |  |  |  |
| `appointment:mark_no_show` | ✓ | ✓ | ✓ | ✓ |  |  |
| `file:read` | ✓ | ✓ | ✓ | ✓ |  | ✓ |
| `file:upload` | ✓ | ✓ | ✓ | ✓ |  |  |
| `file:remove` | ✓ | ✓ |  |  |  |  |
| `report:read` | ✓ | ✓ |  |  |  | ✓ |
| `report:export` | ✓ | ✓ |  |  |  | ✓ |
| `audit:read` | ✓ |  |  |  |  | ✓ |

## 4. Regras de aplicação

1. A role atribui permissões somente no Membership e Tenant atual.
2. O frontend pode esconder ações, mas o backend deve validar a permission em toda operação.
3. Permissões de Patient, File, Report e Audit não dispensam o Tenant Context ou regras de minimização de dados.
4. Funções financeiras permanecem fora do MVP; a role `FINANCE` não recebe permissões operacionais neste catálogo.
5. A criação do administrador inicial concede `TENANT_ADMIN`.
6. Remover a última capacidade administrativa ativa do Tenant é bloqueado.

## 5. Casos mínimos de autorização

- `RECEPTION` cria e confirma Appointment, mas não conclui nem arquiva Patient.
- `PROFESSIONAL` conclui Appointment, mas não gerencia Memberships.
- `AUDITOR` consulta Patient, Agenda, relatórios e auditoria, sem alterar registros.
- `TENANT_ADMIN` administra seu Tenant, sem acesso a qualquer outro Tenant.
- `FINANCE` não acessa dados financeiros até que o domínio Financeiro seja implementado e a matriz seja ampliada.

## Documentos relacionados

- [Regras de Negócio](business-rules.md)
- [Modelo de Domínio](domain-model.md)
- [Critérios de Aceite do MVP](acceptance-criteria.md)
