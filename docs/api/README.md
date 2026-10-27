# API

Contrato e padrões HTTP do ORDIA.

## Fonte de verdade

- [OpenAPI do MVP](openapi-mvp.yaml): schemas, exemplos e respostas dos fluxos iniciais.
- [Contratos REST do MVP](mvp-contracts.md): catálogo de endpoints e permissions.
- [Arquitetura da API](../architecture/api.md): princípios técnicos.

Nenhum desses documentos significa que os endpoints já existem.

## Convenções

- Base pública: `/api/v1`.
- JSON em requests/responses, exceto upload/download.
- Endpoints protegidos usam `Authorization: Bearer <access-token>`.
- O Tenant Context vem da sessão validada; nunca de um `tenantId` confiado ao cliente.
- Listagens usam `page` e `pageSize`, máximo 100.
- DTOs não expõem entidades de persistência.

## Status e erros

| Situação | HTTP |
|---|---:|
| Sem credencial, token inválido ou expirado | 401 |
| Tenant, Membership ou permission insuficiente | 403 |
| Recurso inexistente ou fora de escopo | 404 |
| Conflito de agenda, estado ou integridade | 409 |
| Entrada inválida | 400 ou 422 |
| Limite de uso excedido | 429 |

Erros seguem o schema `Error` no OpenAPI, com `code`, mensagem segura, `traceId` e, quando aplicável, campos inválidos. Nunca incluem stack trace, SQL, credenciais ou segredo.

## Compatibilidade

Adicionar campo opcional ou endpoint é a forma preferencial de evoluir. Alterar semântica, remover campo ou mudar resposta incompatível exige versão/estratégia documentada.

## Verificação futura

Na Fase 3, a especificação deve validar requests/responses e gerar ou alimentar testes de contrato, autenticação, autorização, isolamento de Tenant, conflitos e paginação.
