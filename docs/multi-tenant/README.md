# Multi-Tenant

Estratégia de isolamento e governança de organizações no ORDIA.

O modelo Multi-Tenant é uma característica central do ORDIA. A plataforma poderá atender múltiplas organizações utilizando infraestrutura compartilhada, mantendo seus dados, usuários, configurações e operações logicamente isolados.

## 1. Terminologia

- **Tenant:** organização atendida pela plataforma.
- **Tenant ID:** identificador único da organização dentro do contexto do sistema.
- **Usuário:** identidade que pode estar vinculada a um ou mais contextos organizacionais conforme as regras futuras do produto.
- **Tenant Context:** contexto da organização associado à operação atual.
- **Recurso tenant-owned:** recurso cujo acesso pertence a uma organização específica.

## 2. Regra absoluta

> Um Tenant nunca pode acessar dados pertencentes a outro Tenant.

Essa regra vale para:

- HTTP requests;
- endpoints REST;
- consultas ao banco;
- cache;
- arquivos;
- jobs e tarefas assíncronas;
- eventos internos;
- relatórios;
- integrações externas;
- operações administrativas sujeitas a escopo.

## 3. Identificação do Tenant

O contexto do Tenant deverá ser determinado a partir de uma fonte confiável do lado do servidor.

Fluxo conceitual:

```text
Request
  ↓
Authentication
  ↓
Authenticated User
  ↓
Resolve Tenant Context
  ↓
Validate Membership
  ↓
Authorization
  ↓
Application Service
  ↓
Repository
```

Um `tenant_id` enviado pelo cliente nunca deve ser considerado suficiente para autorizar acesso. O servidor deve validar que o usuário possui vínculo e permissão para atuar naquele Tenant.

## 4. Modelo de dados

Recursos pertencentes a um Tenant devem possuir `tenant_id` explícito quando aplicável.

Modelo conceitual:

```text
Tenant
├── Users / Memberships
├── Roles
├── Permissions
├── Patients
├── Appointments
├── Billing Records
├── Files
├── Reports
└── Audit Events
```

Exemplo de entidade:

```text
Patient
- id
- tenant_id
- name
- created_at
- updated_at
```

## 5. Isolamento no banco

Consultas de recursos tenant-owned devem considerar o contexto do Tenant.

Exemplos conceituais de índices:

```text
(tenant_id, id)
(tenant_id, created_at)
(tenant_id, name)
```

A camada de persistência deve ser projetada para reduzir o risco de consultas sem escopo de Tenant.

Não é permitido depender apenas de filtros adicionados manualmente em cada controller.

## 6. Repositórios e aplicação

O contexto de Tenant deve atravessar as camadas da aplicação.

```text
Controller
   ↓
Application Service
   ↓
Domain
   ↓
Repository
   ↓
Database
```

Controllers não devem ser a única barreira de isolamento. Casos de uso e mecanismos de persistência devem preservar o contexto necessário.

## 7. Usuários, papéis e permissões

A autorização deve considerar pelo menos:

```text
User → Tenant Membership → Role → Permission → Resource
```

Uma permissão em um Tenant não implica automaticamente a mesma permissão em outro.

O modelo deve permitir que uma mesma identidade, caso essa capacidade seja adotada, possua vínculos e permissões diferentes em organizações diferentes.

## 8. Cache

Chaves de cache devem ser projetadas para impedir colisão entre Tenants.

Exemplo:

```text
tenant:{tenant_id}:patients:{patient_id}
tenant:{tenant_id}:settings
```

Nunca armazenar um recurso tenant-owned em uma chave global que permita retorno indevido para outro contexto.

## 9. Jobs e processamento assíncrono

Jobs devem carregar contexto suficiente para determinar o Tenant da operação.

Exemplo:

```text
Job
├── job_id
├── tenant_id
├── actor_id (quando aplicável)
└── payload
```

Workers não devem depender de contexto HTTP para descobrir o Tenant.

## 10. Arquivos

Objetos armazenados em S3 ou compatível devem possuir organização lógica por Tenant.

Exemplo conceitual:

```text
tenants/{tenant_id}/patients/{patient_id}/...
```

A existência de um caminho contendo `tenant_id` não substitui autorização. Toda operação de leitura, gravação ou exclusão deve validar o contexto e a permissão.

## 11. Relatórios e exportações

Relatórios, buscas globais e exportações devem respeitar o Tenant da sessão e o escopo autorizado.

Processos de exportação assíncronos devem manter o contexto do Tenant durante todo o ciclo de geração e entrega do arquivo.

## 12. Auditoria

Eventos de auditoria devem registrar o Tenant quando a operação estiver vinculada a uma organização.

Campos conceituais:

```text
timestamp
tenant_id
actor_id
action
resource_type
resource_id
result
metadata mínima
```

Dados sensíveis devem ser evitados em metadados de auditoria quando não forem necessários.

## 13. Testes de isolamento

O isolamento Multi-Tenant deve possuir testes automatizados.

Casos mínimos:

- usuário do Tenant A não acessa recurso do Tenant B;
- ID válido do Tenant B não funciona no contexto do Tenant A;
- filtros e paginação não retornam dados de outro Tenant;
- cache não cruza contextos;
- jobs processam somente o Tenant esperado;
- arquivos não podem ser acessados fora do escopo;
- relatórios e exportações respeitam o Tenant;
- permissões de um Tenant não são reutilizadas indevidamente em outro.

## 14. Cenários de falha

Devem ser tratados como falhas críticas de segurança:

- ausência inesperada de Tenant Context;
- tentativa de acessar recurso sem `tenant_id` quando ele é obrigatório;
- divergência entre Tenant do usuário e Tenant do recurso;
- acesso por ID direto a recurso de outro Tenant;
- cache hit de outro Tenant;
- job sem contexto de Tenant;
- exportação com escopo incorreto.

O comportamento preferencial nesses casos é negar a operação e registrar o evento técnico apropriado sem expor dados.

## 15. Administração e operações internas

Operações administrativas com acesso potencialmente transversal devem possuir escopo explícito e controles adicionais.

Uma função administrativa não deve ser interpretada automaticamente como permissão irrestrita para consultar qualquer dado. A necessidade e o escopo devem ser definidos pelo produto e pela política de segurança.

## 16. Checklist de implementação

- [ ] Tenant possui identificador único.
- [ ] Tenant Context é resolvido no backend.
- [ ] Membership do usuário é validado.
- [ ] Recursos tenant-owned possuem escopo explícito.
- [ ] Queries críticas consideram `tenant_id`.
- [ ] Cache possui namespace por Tenant.
- [ ] Jobs carregam contexto de Tenant.
- [ ] Arquivos respeitam Tenant e autorização.
- [ ] Auditoria registra Tenant quando aplicável.
- [ ] Testes negativos de isolamento existem.
- [ ] Relatórios e exportações foram testados contra vazamento entre Tenants.

## Documentos relacionados

- [Arquitetura](../architecture/README.md)
- [Segurança](../security/README.md)
- [API](../api/README.md)
- [Documento Mestre](../master/documento-mestre.md)
