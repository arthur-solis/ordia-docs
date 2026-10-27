# Arquitetura

Documentação da arquitetura técnica do ORDIA.

## Diretriz arquitetural

O ORDIA adotará inicialmente uma arquitetura de **Modular Monolith**, mantendo fronteiras claras entre domínios e permitindo futura extração de módulos para serviços independentes quando houver justificativa técnica e de negócio.

A arquitetura deve privilegiar simplicidade operacional, baixo acoplamento, segurança, testabilidade e evolução incremental. A adoção de microserviços não é considerada requisito inicial.

## Visão geral

```text
┌──────────────────────────────────────────────┐
│                  Cliente                     │
│ Desktop · Notebook · Tablet · Smartphone     │
└──────────────────────┬───────────────────────┘
                       │ HTTPS
                       ▼
┌──────────────────────────────────────────────┐
│              SvelteKit Frontend              │
│       UI · Rotas · Estado · API Client       │
└──────────────────────┬───────────────────────┘
                       │ REST / JSON
                       ▼
┌──────────────────────────────────────────────┐
│          ORDIA API · Spring Boot             │
│                                              │
│ Identity │ Tenancy │ Patients │ Scheduling   │
│ Billing  │ Reporting │ Files │ Shared        │
└───────┬──────────────┬───────────────┬───────┘
        │              │               │
        ▼              ▼               ▼
     MySQL           Redis       S3 / compatível
```

## Camadas do backend

Cada módulo deve respeitar responsabilidades bem definidas:

```text
module/
├── api/
├── application/
├── domain/
└── infrastructure/
```

- **api**: controllers, requests, responses e contratos externos.
- **application**: casos de uso e orquestração das operações.
- **domain**: regras de negócio, entidades, objetos de valor e eventos de domínio.
- **infrastructure**: persistência, integrações e detalhes tecnológicos.

O código compartilhado deve permanecer em `shared/` apenas quando houver uma necessidade real de compartilhamento. `shared/` não deve se transformar em um depósito genérico de código.

## Módulos de domínio iniciais

```text
backend/
└── src/main/java/br/com/ordia/
    ├── identity/
    ├── tenancy/
    ├── patient/
    ├── scheduling/
    ├── billing/
    ├── reporting/
    ├── files/
    └── shared/
```

Os módulos representam fronteiras de negócio. Dependências entre módulos devem ser explícitas e controladas.

## Multi-Tenant

O isolamento entre organizações é um requisito arquitetural de primeira classe.

Fluxo mínimo de contexto:

```text
Request
  ↓
Authentication
  ↓
User
  ↓
TenantContext
  ↓
Authorization
  ↓
Application Service
  ↓
Repository
  ↓
Database
```

O contexto do tenant deve acompanhar a operação desde a entrada da requisição até o acesso aos dados. Nenhuma funcionalidade de negócio deve permitir acesso a dados de outro tenant.

Entidades persistidas que pertençam a um tenant devem utilizar `tenant_id` como parte explícita do modelo e das consultas relevantes.

## Autenticação e autorização

A autenticação será baseada em **Spring Security + JWT**.

O JWT poderá carregar informações como:

- `sub`: identificador do usuário;
- `tenant_id`: tenant associado à sessão;
- `roles`: papéis do usuário;
- `permissions`: permissões quando necessário;
- `iat`: instante de emissão;
- `exp`: expiração;
- `jti`: identificador do token.

O token não substitui a fonte de verdade do servidor. Estado do usuário, tenant, permissões e regras de negócio continuam sujeitos à validação no backend.

A autorização será baseada em **RBAC**, evoluindo para permissões granulares e escopo quando necessário:

```text
User → Tenant → Roles → Permissions → Scope
```

## Banco de dados

O banco oficial inicial será **MySQL**.

Entidades multi-tenant devem, quando aplicável, manter metadados como:

- `id`
- `tenant_id`
- `created_at`
- `updated_at`
- `created_by`
- `updated_by`

Índices devem considerar o tenant nas consultas de alto volume, por exemplo:

```text
(tenant_id, id)
(tenant_id, created_at)
(tenant_id, name)
```

A estratégia de banco deve ser definida de modo a impedir vazamento de dados entre tenants por falha de filtro.

## Cache

**Redis** será utilizado quando houver necessidade comprovada de cache, controle de sessão, dados temporários, rate limiting ou outras operações adequadas ao modelo chave-valor.

O Redis não deve ser utilizado como substituto do banco de dados transacional sem decisão arquitetural explícita.

## Armazenamento

Arquivos e objetos binários devem utilizar **S3 ou armazenamento compatível**, mantendo no banco apenas os metadados necessários.

O acesso aos objetos deve respeitar o tenant e as permissões do usuário.

## API

A comunicação externa inicial será baseada em **REST/JSON**, documentada com **OpenAPI/Swagger**.

Princípios:

- contratos claros;
- versionamento quando necessário;
- respostas consistentes;
- validação de entrada;
- tratamento padronizado de erros;
- autenticação e autorização em endpoints protegidos;
- nenhuma exposição direta da estrutura interna do domínio.

GraphQL, brokers de mensagens e outras formas de comunicação não fazem parte da arquitetura inicial sem justificativa registrada.

## Eventos e processamento assíncrono

O monólito poderá utilizar eventos internos de domínio para desacoplar operações, por exemplo:

- `AppointmentCreated`
- `AppointmentConfirmed`
- `AppointmentCancelled`
- `PatientCreated`
- `UserDeactivated`
- `PaymentCreated`

Inicialmente, esses eventos podem permanecer dentro da aplicação. A adoção futura de um broker deve ocorrer apenas quando requisitos de escala, integração ou confiabilidade justificarem a complexidade adicional.

## Frontend

O frontend será organizado por domínio e componentes reutilizáveis:

```text
frontend/
└── src/
    ├── routes/
    ├── lib/
    │   ├── auth/
    │   ├── tenancy/
    │   ├── patients/
    │   ├── scheduling/
    │   ├── billing/
    │   └── shared/
    ├── components/
    │   ├── ui/
    │   ├── forms/
    │   ├── tables/
    │   └── layouts/
    └── services/
```

O frontend não deve reproduzir regras de segurança do backend como se fossem a autoridade final. Validações de UX podem existir no cliente, mas autorização real deve ser garantida pelo servidor.

## Infraestrutura

A estrutura inicial prevista é:

```text
infrastructure/
├── docker/
├── nginx/
├── mysql/
├── redis/
├── s3/
├── monitoring/
└── environments/
    ├── development/
    ├── staging/
    └── production/
```

Os ambientes devem ser tratados de forma reproduzível, evitando configurações manuais sempre que possível.

## Observabilidade

A plataforma deverá evoluir para possuir:

- logs estruturados;
- métricas;
- rastreamento de erros;
- health checks;
- monitoramento de infraestrutura;
- auditoria de operações relevantes.

Observabilidade deve permitir identificar tenant, usuário, módulo e operação envolvidos sem registrar dados sensíveis desnecessariamente.

## Escalabilidade

A estratégia inicial é escalar o monólito horizontalmente quando necessário, mantendo a aplicação stateless sempre que possível.

A extração de um módulo para serviço independente será considerada somente quando houver uma razão concreta, como:

- necessidade de escala independente;
- isolamento de falhas;
- ciclo de implantação independente;
- requisitos tecnológicos incompatíveis;
- integração externa de alta complexidade;
- limites claros de domínio.

A modularização interna deve vir antes da distribuição física dos serviços.

## Decisão arquitetural

A escolha do Modular Monolith como arquitetura inicial está registrada em:

[`docs/decisions/ADR-0001-modular-monolith.md`](../decisions/ADR-0001-modular-monolith.md)

## Documentos relacionados

- [Documento Mestre](../master/documento-mestre.md)
- [Segurança](../security/README.md)
- [Multi-Tenant](../multi-tenant/README.md)
- [API](../api/README.md)
- [Modelo físico do MVP](data-model-mvp.md)
- [Estratégia de migrations](migrations.md)
- [Decisões Arquiteturais](../decisions/README.md)
