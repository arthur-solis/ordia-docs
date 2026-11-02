# Documentação ORDIA

A documentação oficial do ORDIA fica centralizada nesta pasta.

## Mapa

- [Documento Mestre](master/documento-mestre.md): visão e escopo.
- [Produto](product/README.md): requisitos, regras, modelo e decisões do MVP.
- [Arquitetura](architecture/README.md): arquitetura técnica, incluindo [modelo físico](architecture/data-model-mvp.md) e [migrations](architecture/migrations.md).
- [Segurança](security/README.md): controles e [privacidade/LGPD operacional](security/privacy-mvp.md).
- [Multi-Tenant](multi-tenant/README.md): isolamento entre organizações.
- [API](api/README.md): convenções, [catálogo REST](api/mvp-contracts.md) e [OpenAPI inicial](api/openapi-mvp.yaml).
- [Identidade Visual](brand/README.md).
- [Decisões Arquiteturais](decisions/README.md).

## Hierarquia de fontes

1. Documento Mestre: visão de alto nível.
2. Produto: comportamento, regras e decisões do MVP.
3. Arquitetura, Segurança e API: realização técnica coerente com o produto.
4. OpenAPI: contrato verificável da API.

## Estado atual

A documentação 0.2 descreve a implementação candidata da PR de remediação. A main e a versão implantada podem conter uma versão anterior. O código e os testes permanecem privados.
Consulte o [estado de implementação](product/implementation-status.md) e a [decisão de conteúdo privado](decisions/ADR-0002-private-content-mvp.md).
