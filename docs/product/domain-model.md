# Modelo de Domínio Inicial

Modelo conceitual dos principais elementos do ORDIA. Não é ainda um modelo físico de banco de dados.

## 1. Princípios

- O domínio deve refletir regras de negócio, não apenas tabelas.
- Recursos pertencentes a uma organização devem possuir escopo de Tenant.
- Identidade e tenancy são conceitos relacionados, mas não devem ser confundidos.
- Agendamento deve representar estados e regras de transição.
- Dados sensíveis devem possuir acesso explícito.

## 2. Entidades centrais

```text
Platform
   │
   └── Tenant
        ├── Membership ── User
        │                  ├── Role
        │                  └── Permission
        │
        ├── Patient
        │     └── Patient data / history
        │
        ├── Professional / Resource
        │     └── Availability
        │
        ├── Appointment
        │     ├── Patient
        │     └── Professional / Resource
        │
        ├── File
        │
        ├── Report
        │
        └── AuditEvent
```

## 3. Tenant

Representa a organização que utiliza o ORDIA.

Responsabilidades conceituais:

- identidade da organização;
- configurações;
- status;
- políticas específicas;
- relacionamento com usuários e recursos.

## 4. User

Representa a identidade de acesso de uma pessoa.

Possíveis atributos conceituais:

```text
id
name
email
status
created_at
updated_at
```

Credenciais e dados de autenticação devem ser tratados conforme o modelo de segurança e não devem ser confundidos com dados de perfil.

## 5. Membership

Representa o vínculo entre um usuário e um Tenant.

Esse conceito é importante para permitir que permissões sejam atribuídas dentro de um contexto organizacional.

```text
Membership
- id
- tenant_id
- user_id
- status
- roles
```

Uma identidade não deve ganhar acesso a um Tenant apenas por conhecer seu identificador.

## 6. Role e Permission

**Role** agrupa permissões para facilitar administração.

**Permission** representa uma capacidade específica.

Modelo:

```text
User
  ↓
Membership
  ↓
Role
  ↓
Permission
```

Permissões deverão evoluir para um catálogo explícito conforme os módulos forem implementados.

## 7. Patient

Representa a pessoa atendida ou administrada pela organização.

O modelo definitivo deverá distinguir claramente:

- identificação;
- dados de contato;
- dados demográficos necessários;
- dados assistenciais, quando existirem;
- histórico;
- documentos/anexos.

Nem todo dado de paciente deve ser colocado em uma única entidade. O modelo deverá evoluir conforme os requisitos de cada domínio.

## 8. Professional / Resource

Representa um profissional ou recurso necessário à operação da agenda.

A separação exata entre profissional, equipe, sala, equipamento ou outro recurso deverá ser definida antes da implementação de regras avançadas de disponibilidade.

## 9. Appointment

Representa um compromisso agendado.

Conceitos mínimos:

```text
id
tenant_id
patient_id
professional/resource_id
start_at
end_at
status
created_at
updated_at
```

Estados iniciais possíveis:

```text
SCHEDULED
CONFIRMED
CANCELLED
COMPLETED
NO_SHOW
```

As transições permitidas devem ser definidas como regra de domínio, e não apenas como valores livres de banco.

## 10. File

Representa metadados de um objeto armazenado externamente.

```text
File
- id
- tenant_id
- owner_type
- owner_id
- storage_key
- filename
- content_type
- size
- created_at
```

O objeto físico fica no armazenamento S3/compatível. O domínio mantém o vínculo e os metadados necessários.

## 11. AuditEvent

Representa um evento relevante para rastreabilidade.

```text
AuditEvent
- id
- tenant_id
- actor_id
- action
- resource_type
- resource_id
- timestamp
- metadata
```

O conteúdo deve ser suficiente para investigação sem transformar a auditoria em depósito indiscriminado de dados sensíveis.

## 12. Relacionamentos essenciais

```text
Tenant 1 ─── N Membership
User   1 ─── N Membership

Tenant 1 ─── N Patient
Tenant 1 ─── N Appointment
Tenant 1 ─── N Professional/Resource

Patient 1 ─── N Appointment
Professional/Resource 1 ─── N Appointment

Tenant 1 ─── N File
Tenant 1 ─── N AuditEvent
```

## 13. Invariantes iniciais

### INV-01
Todo recurso tenant-owned deve pertencer a exatamente um Tenant no contexto normal de operação.

### INV-02
Um usuário só pode operar em um Tenant quando possuir vínculo e autorização válidos.

### INV-03
Um agendamento deve possuir referências válidas aos participantes obrigatórios do fluxo.

### INV-04
Uma transição de estado de agendamento deve ser válida segundo as regras de domínio.

### INV-05
Um recurso não pode ser acessado fora do escopo autorizado apenas porque seu ID é conhecido.

### INV-06
Operações críticas devem manter rastreabilidade quando exigido pelo domínio ou segurança.

## 14. O que ainda não está fechado

O modelo não define ainda detalhes como:

- prontuário clínico completo;
- especialidades;
- convênios;
- procedimentos;
- faturamento;
- estoque;
- unidades/filiais;
- equipes complexas;
- notificações;
- integrações externas.

Esses pontos devem ser adicionados somente quando os requisitos forem definidos.


## 15. Refinamentos do MVP

As decisões do MVP fecham os seguintes pontos do modelo conceitual:

### 15.1 Estados

| Entidade | Estados do MVP |
|---|---|
| User | `ACTIVE`, `DISABLED` |
| Tenant | `PENDING`, `ACTIVE`, `SUSPENDED`, `CLOSED` |
| Membership | `PENDING`, `ACTIVE`, `SUSPENDED`, `REVOKED` |
| Patient | `ACTIVE`, `ARCHIVED` |
| Professional/Resource | `ACTIVE`, `INACTIVE` |
| Appointment | `SCHEDULED`, `CONFIRMED`, `CANCELLED`, `COMPLETED`, `NO_SHOW` |
| Exportation | `PENDING`, `RUNNING`, `COMPLETED`, `FAILED`, `EXPIRED` |

### 15.2 Resource

O modelo do MVP utiliza uma entidade conceitual `Resource` com tipos `PROFESSIONAL`, `ROOM` e `EQUIPMENT`. Cada recurso pertence a um Tenant, possui capacidade unitária e pode possuir horários de trabalho e bloqueios. O vínculo entre `User` e `Resource(PROFESSIONAL)` é opcional e não automático.

### 15.3 Appointment

Um Appointment do MVP possui um Patient `ACTIVE`, pelo menos um Resource `PROFESSIONAL` `ACTIVE`, e opcionalmente Resource de sala ou equipamento. O intervalo segue `[start_at, end_at)`, é armazenado em UTC e é avaliado contra a disponibilidade dos recursos do mesmo Tenant.

### 15.4 Patient

O cadastro mínimo inclui nome completo, data de nascimento e ao menos um meio de contato. Documento é opcional. Possível duplicidade é identificada por documento normalizado ou, na ausência dele, por nome normalizado e data de nascimento; o alerta não bloqueia o cadastro nem aciona mesclagem automática.

### 15.5 File e Exportation

File armazena metadados e vínculo com recurso proprietário; o objeto físico é externo e possui chave gerada pelo servidor com namespace de Tenant. Exportation é um artefato derivado, associado ao Tenant, solicitante, filtros, estado e File resultante quando concluída.

### 15.6 Referências

- [Decisões do MVP](mvp-decisions.md)
- [Matriz de Acesso](access-control.md)
- [Contratos do MVP](../api/mvp-contracts.md)
