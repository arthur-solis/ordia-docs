# Arquitetura Multi-Tenant

## Objetivo

Garantir que múltiplas organizações utilizem a mesma plataforma ORDIA sem acesso indevido aos dados umas das outras.

## Modelo

O modelo inicial será de **isolamento lógico por tenant**.

```text
ORDIA
│
├── Tenant A
│   ├── Users
│   ├── Patients
│   ├── Appointments
│   └── Billing
│
├── Tenant B
│   ├── Users
│   ├── Patients
│   ├── Appointments
│   └── Billing
│
└── Tenant C
    ├── Users
    ├── Patients
    ├── Appointments
    └── Billing
```

## TenantContext

Cada requisição autenticada deve estabelecer o contexto do tenant antes da execução das operações protegidas.

```text
JWT
 ↓
User
 ↓
TenantContext
 ↓
Authorization
 ↓
Use Case
 ↓
Tenant-scoped Repository
```

O `TenantContext` deve ser tratado como contexto confiável somente após validação da autenticação e das relações do usuário com o tenant.

## Isolamento

A regra absoluta é:

> Um tenant nunca pode ler, alterar, excluir ou inferir indevidamente dados pertencentes a outro tenant.

O isolamento deve existir no backend e não pode depender apenas de filtros implementados no frontend.

## Dados

Entidades tenant-scoped devem utilizar `tenant_id` como parte explícita do modelo quando aplicável.

Repositórios e casos de uso devem impedir operações sem contexto de tenant quando o recurso exigir isolamento.

## Autorização

Estar autenticado não significa possuir acesso a todos os recursos do tenant.

A autorização deve considerar:

```text
User
 ↓
Tenant membership
 ↓
Role
 ↓
Permission
 ↓
Resource / Scope
```

## Operações entre tenants

Operações cross-tenant não fazem parte do fluxo comum da aplicação.

Quando uma operação administrativa futura exigir acesso global, ela deverá possuir escopo e autorização explícitos, além de auditoria adequada.

## Testes de isolamento

O isolamento deve possuir testes automatizados que tentem, no mínimo:

- consultar recurso de outro tenant;
- alterar recurso de outro tenant;
- excluir recurso de outro tenant;
- acessar endpoint sem tenant válido;
- utilizar token associado a outro tenant;
- explorar IDs conhecidos ou previsíveis de outro tenant.

Qualquer vazamento de dados entre tenants deve ser tratado como falha crítica de segurança.
