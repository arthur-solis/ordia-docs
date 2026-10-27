# Autorização

## Fonte de verdade

A [Matriz de Acesso do MVP](../product/access-control.md) define roles e permissions. As [Regras de negócio](../product/business-rules.md) definem os estados e o isolamento.

## Modelo

O MVP usa RBAC por Tenant:

```text
User → Membership ativa no Tenant → Roles → Permissions → recurso do Tenant
```

Roles iniciais: `TENANT_ADMIN`, `MANAGER`, `PROFESSIONAL`, `RECEPTION`, `FINANCE` e `AUDITOR`. Não existem roles customizáveis no MVP.

## Decisão por requisição

1. autenticar a credencial;
2. resolver o Tenant Context validado;
3. confirmar User, Tenant e Membership ativos;
4. exigir a permission da matriz;
5. limitar a consulta/comando ao Tenant;
6. aplicar regra específica do recurso.

Ocultar controles no frontend não concede nem revoga acesso.

## Escopo e auditoria

O escopo obrigatório no MVP é o Tenant. Escopos por unidade, proprietário ou recurso são evolução futura e exigem decisão registrada. Mudanças de Membership, roles e permissões, além de ações sensíveis, são auditadas sem incluir segredos.
