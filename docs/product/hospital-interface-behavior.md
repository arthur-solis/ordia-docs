# DEC-HOSP-009 · Comportamentos comuns e ações restritas
Planejamento consolidado em 19/11/2026. Complementa o [mapa de navegação](screen-map-navigation.md).

| Situação | Comportamento esperado |
|---|---|
| Carregamento | Indicar progresso e impedir submissões repetidas |
| Lista vazia | Distinguir ausência de registros de filtros sem resultado; oferecer cadastro apenas se permitido |
| Campo inválido | Explicar junto ao campo e preservar o preenchimento |
| Sucesso | Mensagem curta e atualização do estado apresentado |
| Falha ao salvar | Explicar a falha, conservar dados e permitir nova tentativa |
| Conflito de agenda | Informar indisponibilidade; remarcação recusada preserva reserva original |
| Acesso negado | Informar e permitir retorno a uma área autorizada |
| Sessão expirada | Pedir login novamente e informar sobre preenchimentos a refazer |
| Exportação | Exibir andamento e liberar download somente quando pronto e autorizado |
| Alterações pendentes | Avisar ao sair; continuar editando ou descartar |
| Edição concorrente | Avisar antes de sobrescrever; permitir conferir a versão atual |

Mensagens combinam texto e indicação visual. Identificação do paciente e do atendimento permanece visível nos fluxos correspondentes. Revisão por teclado, contraste, foco e dispositivos faz parte da etapa 16, ainda pendente.

## Responsabilidade por ações
| Ação | Quem executa | Papel da recepção |
|---|---|---|
| Cancelar agendamento | Gestão de contas autorizada | Solicitar e acompanhar |
| Arquivar paciente | Gestão de contas autorizada | Sem execução direta |
| Suspender acesso de funcionário | TI do hospital | Sem execução direta |
| Analisar cancelamento do registro de atendimento | Gestão de contas autorizada | Solicitar com motivo e acompanhar |

Cada ação restrita exige autorização no servidor, confirmação do registro e consequência, motivo e auditoria. Os pares perfil–setor são atribuições explícitas, sem produto cartesiano de perfis e setores.

## Registro de atendimento e cancelamento
O termo “guia” usado nas primeiras telas de recepção referia-se ao registro interno de atendimento. A decisão posterior é identificá-lo como atendimento, separando da guia TISS.

A recepção pede cancelamento e acompanha os estados internos propostos **Pendente → Em análise → Aprovada ou Recusada**. Esses estados não são códigos TISS. A existência de documentos ou registros assistenciais não impede o encaminhamento à análise.

Aprovar o cancelamento interno cancela e arquiva o registro, preservando documentos, registros clínicos e histórico; sua consulta fica restrita a quem tem autorização. Não apagar nem liberar acesso clínico à recepção.

Cancelar uma guia já transmitida à operadora constitui outro processo: solicitação externa e resposta da operadora, com histórico próprio. A aprovação interna não comprova cancelamento externo. Veja [atendimento e TISS](hospital-attendance-tiss.md).

## Implementação
As restrições acima substituem a regra inicial de cancelamento direto pela recepção no planejamento hospitalar. A matriz técnica da base permanece histórica até conferência e ajuste do código na etapa 18.

