# Arquitetura da API

## Padrão

A API inicial do ORDIA é REST/JSON, implementada com Spring Boot e documentada por OpenAPI.

## Contrato e versionamento

O namespace público inicial é **`/api/v1`**. A versão representa o contrato externo: mudanças incompatíveis exigem evolução planejada e documentada; adições compatíveis devem preservar consumidores existentes.

A fonte operacional é [OpenAPI do MVP](../api/openapi-mvp.yaml). O [catálogo REST](../api/mvp-contracts.md) mantém a cobertura funcional e a [API](../api/README.md) define convenções transversais.

## Princípios

- DTOs separados de entidades de persistência;
- validação no limite HTTP e regras no domínio/aplicação;
- erros estruturados, sem detalhes internos;
- autenticação, autorização e Tenant Context antes do caso de uso;
- contratos e exemplos atualizados junto dos endpoints reais;
- testes de contrato, isolamento e cenários de erro na implementação.

## Fluxo

```text
HTTP Request → Validation → Authentication → Tenant Context → Authorization
→ Application Service → Domain → Repository → HTTP Response
```

REST é a estratégia inicial. GraphQL, gRPC e mensageria exigem necessidade comprovada e decisão arquitetural.
