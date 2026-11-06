# Cenário hospitalar e visão do produto
Data: 05/11/2026. Decisões de cenário de 02/11 e perfis de 03/11 consolidados com o mapa inicial de telas e navegação aprovado em 05/11.

## Cenário aprovado
O Ordia será um sistema de gestão para hospitais gerais privados, contemplando processos administrativos e assistenciais, com atendimento a pacientes particulares e beneficiários de convênios.
O cenário inicial não contempla SUS. O acesso é exclusivo de funcionários autorizados; portal do paciente fica para uma etapa futura. Perfis externos e acesso autônomo por pacientes não integram o mapa atual.

## Abrangência da visão hospitalar
| Área | Processos a detalhar |
|---|---|
| Recepção e pacientes | Identificação, cadastro, entrada e encaminhamento |
| Ambulatório | Consultas, agendas e acompanhamento |
| Urgência e emergência | Triagem, classificação de risco e atendimento |
| Internação | Admissão, leitos, transferências e alta |
| Prontuário | Evoluções, diagnósticos, prescrições e histórico |
| Enfermagem | Avaliações, cuidados, sinais vitais e administração de medicamentos |
| Farmácia | Estoque, dispensação, devoluções e movimentações |
| Exames | Solicitação, coleta quando aplicável, execução e resultados laboratoriais e de imagem |
| Centro cirúrgico | Programação, salas, equipe, materiais e registros de procedimentos |
| Gestão hospitalar | Profissionais, setores, recursos, materiais e equipamentos |
| Financeiro e faturamento | Contas hospitalares, convênios, cobranças e pagamentos |
| Administração e segurança | Instituições, usuários, acessos, auditoria e relatórios |

Para convênios, o planejamento inclui operadoras, planos, cobertura, autorizações e guias. Para particulares, inclui preços, orçamentos, pagamentos e cobranças.
A conta hospitalar deverá relacionar consultas, diárias, procedimentos, exames, medicamentos e materiais utilizados. O faturamento deverá acompanhar cobranças, recusas, ajustes e recebimentos.
Esses pontos são direcionadores de produto; regras detalhadas e interfaces com operadoras ainda não foram aprovadas.

## Visão, código e entrega do TCC
- **Visão aprovada:** cobre as áreas hospitalares acima, incluindo financeiro/faturamento. Essa decisão amplia a visão anterior do produto.
- **Base implementada:** identidade, instituições, membros/permissões, pacientes, recursos/disponibilidade, agenda, arquivos, relatórios/exportações e auditoria. Consulte o [estado de implementação](implementation-status.md).
- **Entrega demonstrável do TCC:** o recorte detalhado e a ordem de construção ainda serão definidos por etapas. A visão completa não é uma promessa de que todos os módulos estarão implementados na apresentação.
- **Etapa atual:** planejamento e validação com dados fictícios em ambiente local. Produção e contratação de serviços ficam para depois do TCC.

Os documentos anteriores de MVP, permissões, requisitos e API continuam descrevendo a base existente. Não devem ser interpretados como especificação completa dos novos módulos hospitalares.
Regras clínicas, responsabilidades profissionais e fluxos de convênio precisam de levantamento e validação apropriados antes de implementação; o mapa não define protocolos assistenciais nem comprova conformidade.

## Progresso dos encontros
| Etapa | Estado | Entrega |
|---|---|---|
| 1 · Cenário e visão | Definido | Hospital geral privado, convênios e particulares; recorte detalhado do TCC pendente |
| 2 · Perfis e responsabilidades | Base aprovada | [Perfis hospitalares](hospital-user-profiles.md); permissões por operação pendentes |
| 3 · Mapa de telas | Mapa inicial aprovado | [Telas e navegação](screen-map-navigation.md); especificação por módulo pendente |
| 4 · Navegação | Direção aprovada | Ambiente único com menus e painel conforme perfil/permissões, setor e instituição |
| 5 · Identidade visual | Próxima etapa | Cores, tipografia, espaçamentos e componentes a revisar |

## Referências
- [Perfis e responsabilidades](hospital-user-profiles.md)
- [Mapa de telas e navegação](screen-map-navigation.md)
- [MVP da base integrada](mvp.md)
- [Decisão de ampliação e navegação](../decisions/ADR-0004-hospital-scope-navigation.md)
