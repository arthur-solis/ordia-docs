# Atendimento, convênio e preparação de guia
Consolidação dos protótipos e decisões até 19/11/2026. Proposta de produto orientada pelos [materiais ANS fornecidos](tiss-source-register.md); não é declaração de conformidade TISS nem integração em funcionamento.

## Identificadores e contextos separados
Paciente mantém ficha única e número interno no hospital. Cada atendimento possui identificador próprio, distinto dos números de guia no prestador e na operadora. Os exemplos P-000128 e AT-2026-0148 são identificadores internos fictícios.

Na abertura, usar **Regime de atendimento** e **Caráter do atendimento** como campos distintos. No cenário ilustrado: Pronto-socorro e Urgência/Emergência. A linha “Setor” foi retirada do resumo de Dados do atendimento; o contexto de trabalho permanece na barra superior. Não confundir isso com remover os controles de escopo.

Convênio, particular e “A confirmar” são opções de organização interna propostas pelo Ordia. “A confirmar” não é código TISS. Pendências cadastrais não equivalem a elegibilidade positiva.

## Convênio e elegibilidade
Identificação da operadora e contratado vem do cadastro institucional. A recepção informa a carteirinha e dados aplicáveis do beneficiário. Na consulta de elegibilidade, a carteirinha é obrigatória; validade depende de constar na carteira, e validação de presença depende do mecanismo adotado entre prestador e operadora.

Código de validação de presença pode funcionar como um token de presença. Não é senha de login ou autorização automática de procedimentos. Ausência justificada depende das condições e domínio próprios.

Salvar dados incompletos como rascunho é proposta interna; transmitir exige validação específica da mensagem. Exibir “Ainda não consultada” enquanto não houver consulta e resposta. Uma resposta negativa precisa de motivo, conforme mensagem aplicável.

## Médico responsável e solicitante
O responsável pelo atendimento pode estar aguardando atribuição. A atribuição administrativa não substitui a responsabilidade clínica nem gera solicitação de procedimento.

O solicitante da guia deriva da solicitação profissional efetiva e pode ser diferente do responsável pelo atendimento. Identificação profissional, conselho, registro, UF e CBO devem vir dos dados conferidos; nunca preencher com registros inventados. Identificar também o contratado solicitante e seu código junto à operadora, conforme o cenário.

## Preparar guia SP/SADT
1. Vincular paciente, atendimento e solicitação profissional.
2. Preencher identificação da guia, operadora, beneficiário e etapa da autorização.
3. Conferir contratado e profissional solicitante, data, caráter e indicação clínica quando exigida.
4. Adicionar itens: tabela de referência, código, descrição e quantidade solicitada.
5. Completar informações aplicáveis e salvar rascunho.
6. Validar a mensagem completa e encaminhar a quem tiver permissão de envio. O perfil remetente ainda precisa ser detalhado; botão visível na prévia não concede esse direito.
7. Após integração futura, acompanhar envio e resposta sem antecipar autorização.

Na seção complementar, o indicador de recém-nato **é obrigatório para a mensagem de solicitação SP/SADT**, mesmo estando visualmente agrupado em “Dados complementares”. Responder Sim/Não conforme o caso; o rascunho pode permanecer pendente. Código do executante na operadora e CNES são condicionados à solicitação pelo executante. Guia principal se aplica à solicitação SADT de paciente internado. Cobertura especial tem condição própria, não uma escolha genérica livre. Observação/justificativa é opcional e limitada a 500 caracteres nessa mensagem.

## Revisões conhecidas nas imagens
As [telas](../prototypes/README.md) preservam o histórico visual apresentado, sem afirmar que sejam formulários completos para transmissão:
- Preparar guia: corrigir marcações de obrigatoriedade de carteirinha e identificação profissional; o médico responsável do atendimento não é requisito universal da mensagem SP/SADT.
- Incluir de forma visível os dados do contratado solicitante (nome e código), além do profissional, e o registro ANS conferido da operadora.
- Destacar que o indicador de recém-nato precisa ser respondido antes de transmitir; o título “complementares” não o torna opcional.
- Vinculação da solicitação, composição da mensagem, permissões de transmissão, anexos aplicáveis e respostas continuam a detalhar e implementar.
- As telas antigas que usam “Guia” ou prefixo G para um atendimento interno devem ser alinhadas ao vocabulário AT/Atendimento. Não confundir com guia externa TISS.
- Particular exige fluxo próprio; não obriga abertura de guia de convênio.

## Estados independentes
| Processo | O que o estado representa |
|---|---|
| Atendimento interno | Registro operacional do hospital |
| Elegibilidade | Consulta e resposta sobre beneficiário |
| Guia e autorização | Rascunho, envio e resultado efetivo da solicitação |
| Cancelamento interno | Decisão de Gestão de contas sobre registro de atendimento |
| Cancelamento externo | Pedido e resposta da operadora para guia transmitida |

Os rótulos internos não substituem os códigos padronizados. Uma negativa de autorização não elimina o atendimento. Uma análise interna não é resposta da operadora.

## Evidências e próximos passos
A referência SP/SADT está nas páginas 20–23 do Componente de Conteúdo e Estrutura, novembro/2025. A lista de fontes, versões e limitações está no [registro ANS/TISS](tiss-source-register.md). Validação XML/XSD, transporte, credenciais, resposta simulada claramente identificada e testes de contrato precisam ser definidos antes de uma demonstração de integração.

