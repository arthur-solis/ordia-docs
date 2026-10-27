# Arquitetura de Dados

## Banco principal

O banco relacional inicial é MySQL 8.0+. A modelagem privilegia integridade, consistência, índices adequados e isolamento entre Tenants.

## Regras estruturais

- Dados tenant-scoped possuem `tenant_id` explícito.
- Consultas e índices relevantes começam pelo Tenant.
- Integridade crítica é protegida pelo domínio, aplicação e banco.
- Auditoria e exclusões lógicas preservam rastreabilidade.
- Alterações estruturais são reproduzíveis; produção não recebe edição manual.

## Referências normativas

- [Modelo físico inicial do MVP](data-model-mvp.md): tabelas, FKs, índices e regras de concorrência.
- [Estratégia de migrations](migrations.md): Flyway, ordem e evolução segura.
- [Multi-Tenant](../multi-tenant/README.md): exigências de isolamento além do banco.

PostgreSQL, MongoDB ou outro banco não fazem parte do MVP sem decisão arquitetural registrada.
