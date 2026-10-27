# Autenticação

## Fonte de verdade

As regras funcionais estão em [Decisões do MVP](../product/mvp-decisions.md) e [Regras de negócio](../product/business-rules.md). Este documento define sua tradução arquitetural.

## Estratégia

A API usará Spring Security + JWT. O access token dura **15 minutos**; o refresh token dura **30 dias** e é rotacionado a cada uso.

O JWT transporta `sub`, `tenant_id`, `roles`, `iat`, `exp` e `jti`. Não deve conter dados pessoais, senha, token de refresh ou dados excessivamente dinâmicos.

## Fluxo de login

```text
Credenciais → usuário ACTIVE? → Membership ACTIVE? → limite de tentativas?
→ emitir access token + refresh token
```

A falha responde de forma genérica. Após 5 falhas por identificador e origem em 15 minutos, a tentativa é bloqueada por 15 minutos e auditada.

## Autoridade do servidor

O JWT assinado não substitui estado atual. Em toda operação protegida o backend confirma usuário ativo, Tenant ativo, Membership ativa, sessão válida e permission necessária.

## Sessão e revogação

Refresh tokens são armazenados apenas como hash e agrupados em família. Logout, desativação do usuário, suspensão/revogação de Membership, alteração de senha e reset invalidam as sessões atingidas. Reuso de refresh token rotacionado deve invalidar a família e gerar evento de segurança.

## Recuperação de senha

O token de recuperação é de uso único, expira em 30 minutos e é armazenado somente como hash. Um novo pedido invalida o anterior; o fluxo é limitado a 3 pedidos por hora por identificador e origem e não enumera contas.

## Segurança

Senhas usam hash adequado para senha, tokens e senhas nunca entram em logs, e endpoints sensíveis possuem rate limit e auditoria.
