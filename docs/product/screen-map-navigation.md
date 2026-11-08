# Mapa inicial de telas e navegação
Direção aprovada em 05/11/2026. Este é o mapa da visão hospitalar; não é inventário de telas já implementadas.

## Mapa por área
| ID | Área | Telas e espaços de trabalho previstos |
|---|---|---|
| UI-01 | Acesso | Login, recuperação/redefinição de senha, aceitação de convite e seleção/troca de instituição |
| UI-02 | Início | Painel com informações e pendências conforme perfil |
| UI-03 | Pacientes | Busca, cadastro, dados do paciente e histórico de atendimentos |
| UI-04 | Recepção e ambulatório | Agenda, agendamento, chegada e fila de atendimento |
| UI-05 | Pronto-socorro | Entrada, fila de triagem, classificação de risco e acompanhamento |
| UI-06 | Internação e leitos | Mapa de leitos, admissão, internações, transferências e saída administrativa |
| UI-07 | Prontuário | Resumo do atendimento, evoluções, diagnósticos, prescrições, solicitações e alta clínica |
| UI-08 | Enfermagem | Pacientes do setor, avaliações, sinais vitais, cuidados e checagens |
| UI-09 | Farmácia | Prescrições a dispensar, dispensação, devoluções e estoque de medicamentos |
| UI-10 | Exames | Solicitações, filas de execução, coleta quando aplicável e resultados |
| UI-11 | Centro cirúrgico | Programação, procedimentos, salas, equipe e registros cirúrgicos |
| UI-12 | Materiais e estoque | Catálogo, entradas, saídas, transferências e reposição |
| UI-13 | Convênios e autorizações | Operadoras, planos, vínculo do paciente e acompanhamento de autorizações |
| UI-14 | Contas e faturamento | Conta hospitalar, conferência, cobranças, envio ao convênio e recusas/ajustes |
| UI-15 | Financeiro e caixa | Orçamentos particulares, pagamentos e contas a pagar/receber |
| UI-16 | Gestão | Relatórios e indicadores por área |
| UI-17 | Administração | Instituição, setores, profissionais, recursos, disponibilidade, usuários e permissões |
| UI-18 | Auditoria | Consulta das ações registradas, conforme autorização |

Um item pode ser aba, painel ou fluxo dentro de uma tela. Não existe obrigação de criar uma página para cada termo da tabela. A conta hospitalar, a alta clínica e a saída administrativa são conceitos distintos e exigem regras próprias a detalhar.
O [fluxo de acesso aprovado](hospital-access.md) atribui a criação da instituição e o convite inicial da TI ao operador do Ordia. A TI convida os demais funcionários. O [fluxo de Pacientes](hospital-patients.md) detalha busca e cadastro em UI-03 e o cadastro provisório em UI-05. O mapa é de uso interno por funcionários.

## NAV-01 · Ambiente único
Um sistema e um login por sessão, com áreas disponíveis conforme função/permissões, setor e instituição. Administrativo e assistencial compartilham o ambiente; não haverá aplicações separadas para esses grupos nesta direção aprovada.
Quem acumula funções acessa suas áreas sem novo login. O backend valida autorização em cada operação; esconder menu não é barreira de segurança.

## NAV-02 · Estrutura
- Menu lateral por áreas, exibindo opções autorizadas.
- Barra superior com instituição atual, setor quando aplicável e perfil/sair.
- Painel inicial contextual: recepção acompanha chegadas; assistência acompanha pacientes/atendimentos; financeiro acompanha cobranças/recebimentos.
- Troca de instituição revalida vínculo e permissões; o setor selecionado não concede direitos.
- Links diretos seguem as mesmas permissões dos menus.

## NAV-03 · Contexto do trabalho
Caminho central: login → instituição, quando necessário → painel do perfil → área de trabalho → paciente/atendimento, quando aplicável → ação → acompanhamento.
Manter identificação do paciente e contexto do atendimento visíveis durante registros assistenciais, com apresentação dos dados limitada ao acesso autorizado.
Uma solicitação poderá ser acompanhada em Exames; uma prescrição poderá originar trabalho na Farmácia. Essas ligações representam fluxos planejados, ainda sujeitos à definição de estados e regras.
Ao retornar de um detalhe, preservar filtros e período da lista anterior quando ainda válidos e dentro do mesmo contexto autorizado. Ao trocar instituição ou encerrar sessão, limpar contexto e dados anteriores.

## Pendências de detalhamento
- Rotas finais, hierarquia de páginas e relação entre abas/modais.
- Campos, ações, validações e permissões por operação.
- Regras de composição do painel para quem acumula perfis e seleção de setor.
- Estados de carregamento, vazio, erro, conflito, sucesso e acesso negado.
- Protótipos, acessibilidade, responsividade e validação dos fluxos.
- Priorização das telas que integrarão a entrega demonstrável do TCC.

## Referências
- [Cenário hospitalar](hospital-scope.md)
- [Perfis hospitalares](hospital-user-profiles.md)
- [Estado do código](implementation-status.md)
