# API
Contrato 0.2 da base integrada à main. A disponibilidade em execução depende do ambiente e das dependências configuradas. Para o TCC, a referência é a demonstração local com dados fictícios; produção fica para depois.

## Fontes
- [OpenAPI](openapi-mvp.yaml): rotas, entradas, respostas e permissões.
- [Catálogo REST](mvp-contracts.md).
- [Autenticação](../architecture/authentication.md).
- [Matriz de acesso](../product/access-control.md).

## Convenções
Base /api/v1. JSON, exceto upload multipart e download binário. IDs UUID textuais.
Tenant Context deriva da sessão validada. IDs do cliente não dispensam escopo e autorização.
Datas persistidas são UTC, retornadas com offset; horários de trabalho são locais no fuso IANA da instituição.
Paciente exige nome, nascimento não futuro e pelo menos um contato; documento opcional aceita CPF/CNPJ válido.
Senhas: 12 caracteres no cadastro/reset e máximo de 72 bytes UTF-8 para BCrypt.

## Status
| Situação | HTTP |
|---|---:|
| Credencial ausente, inválida, expirada ou sessão inativa | 401 |
| Permissão insuficiente | 403 |
| Recurso inexistente ou fora de escopo | 404 |
| Conflito de estado, duplicidade de e-mail, reserva ou concorrência | 409 |
| JSON/parâmetro inválido | 400 |
| Dados que falham validação | 422 |
| Arquivo acima do limite | 413 |
| Limite temporário excedido | 429 |
| Dependência não configurada/indisponível | 503 |

Erro uniforme: code, message, traceId e fields quando aplicável. X-Trace-Id acompanha a requisição e seus eventos.
Não retornar SQL, stack trace, senha ou token em mensagens de erro.
Listagens de pacientes/relatórios/auditoria usam page/pageSize (máximo 100); agenda e recursos têm limites explícitos no contrato.
A compatibilidade de payload é validada por testes e validação OpenAPI em CI. O catálogo não substitui a verificação da versão implantada.
