# Autorização
Permissões são resolvidas no Membership ativo e no Tenant Context validado. Não há papel transversal no MVP.
O administrador inicial recebe TENANT_ADMIN na mesma transação da criação da instituição.

A versão candidata aplica permissões às operações de Patient, Resource, Appointment, File, Report, Audit e Membership.
Cada operação usa escopo de Tenant em consultas e mutações. Arquivos exigem também leitura do proprietário; relatórios/exportações exigem leitura da fonte.
Downloads revalidam sessão e permissões, inclusive após suspensão ou revogação.
A última capacidade administrativa ativa não pode ser removida/suspensa/revogada pela API. Alterações são serializadas por instituição e auditadas.

Consulte a [matriz de acesso](../product/access-control.md) e os [cenários de aceite](../product/acceptance-criteria.md).
