# Protótipos do Ordia
Atualização: 19/11/2026. Prévia conceitual com dados fictícios, elaborada para planejamento do TCC. As imagens foram produzidas com apoio de geração de imagens e revisadas ao longo do fluxo; não são capturas do código em execução.

## Direção de trabalho atual · 20/11/2026
A criação antecipada de protótipos está **pausada por decisão do autor**. A base existente orientará a implementação; novas telas serão criadas quando o módulo precisar delas. Isso não conclui a revisão dos fluxos nem a responsividade/acessibilidade.

Após este conjunto de 19 imagens, foram discutidos refinamentos SP/SADT, rascunho salvo/PDF, documentos administrativos, histórico e solicitação/acompanhamento de cancelamento. Os arquivos desta galeria ainda não incluem todas essas revisões. O [roteiro](../product/planning-progress.md) e o [plano de adequação](../product/implementation-backlog.md) são o ponto de retomada para desenvolver.

## Como interpretar
“Prévia aprovada” registra a direção discutida no chat, não aprovação clínica, normativa ou de produção. Telas antigas mantidas no conjunto podem exigir alinhamento de vocabulário. O formulário SP/SADT está em revisão e não está completo para transmissão. A lista abaixo registra o estado daquela publicação. Houve revisões posteriores no chat; ela não deve ser interpretada como inventário atualizado de todas as prévias.

Para implementação, prevalecem as regras textuais atualizadas e os materiais ANS indicados em [atendimento/TISS](../product/hospital-attendance-tiss.md), não erros ou omissões gráficos. Não há autorização ou consulta real à operadora nestas imagens.

## Padrão visual
Manter a marca orbital aprovada, wordmark ORDIA com A aberto/ponto turquesa, sem subtítulo “Fusão”; menu lateral azul-marinho amplo, itens espaçados, ícones finos, seleção azul e grafismo orbital inferior. Cartões claros e acentos azul/turquesa. As duas últimas imagens já incorporam a correção do menu.

O nome Fusão identifica a proposta de marca, não um texto a imprimir sob o logo. Não reinterpretar o símbolo em cada tela. A paleta já possui uma proposta separada no [PR de identidade visual](https://github.com/arthur-solis/ordia-docs/pull/6); valores de tokens e componentes continuam a revisar.

## Inventário
| Tela | Estado documental | Observação |
|---|---|---|
| [1. Login](#tela-01) | Direção visual aprovada | Entrada de funcionários; recuperação ainda requer telas próprias. |
| [2. Visão geral da gestão](#tela-02) | Referência visual aprovada | Indicadores fictícios; visão ampla não representa módulos implementados. |
| [3. Equipe](#tela-03) | Prévia aprovada no fluxo | Gestão de acessos pela TI; suspensão não pertence à recepção. |
| [4. Convidar funcionário](#tela-04) | Prévia aprovada no fluxo | Perfis e setores em pares explícitos. |
| [5. Aceitar convite](#tela-05) | Versão revista | Removido o link “Já tenho conta no Ordia”; a regra de conta existente permanece no fluxo de acesso. |
| [6. Painel da recepção](#tela-06) | Prévia aprovada no fluxo | Recepção solicita cancelamento e acompanha, sem executá-lo. |
| [7. Solicitações de cancelamento](#tela-07) | Fluxo aprovado; vocabulário a revisar | A coluna “Guia” nesta imagem representa atendimento interno; não é cancelamento TISS. Identificadores G precisam ser alinhados. |
| [8. Cadastrar paciente](#tela-08) | Prévia aprovada no fluxo | CPF quando existente; alternativa documental e ao menos um contato precisam estar claros na validação final. |
| [9. Possível duplicidade](#tela-09) | Prévia aprovada no fluxo | Conferência humana; sem mesclagem automática de pessoas. |
| [10. Cadastro provisório](#tela-10) | Prévia aprovada no fluxo | Identidade pendente e número interno; regularização com histórico ainda a detalhar. |
| [11. Lista de pacientes](#tela-11) | Prévia aprovada no fluxo | Busca e situações cadastrais; não concede arquivamento à recepção. |
| [12. Ficha do paciente](#tela-12) | Prévia aprovada; vocabulário a revisar | Histórico usa “Guia”/“Abrir guia” para atendimento interno. Corrigir para atendimento na revisão. |
| [13. Novo atendimento](#tela-13) | Versão revista orientada a TISS | Regime separado de caráter. “A confirmar” é estado interno. Não equivale a elegibilidade. |
| [14. Resumo do atendimento](#tela-14) | Versão revista | Sem linha Setor no cartão; médico responsável pode aguardar atribuição. |
| [15. Dados do convênio](#tela-15) | Prévia discutida | Elegibilidade ainda não consultada; presença e validade têm regras próprias. Rascunho não equivale a mensagem validada. |
| [16. Guias e autorizações](#tela-16) | Prévia aprovada no fluxo | Estado vazio; preparar guia não significa transmitir ou autorizar. |
| [17. Definir médico responsável](#tela-17) | Prévia aprovada no fluxo | Registros profissionais demonstrativos; responsável não é automaticamente solicitante. |
| [18. Preparar guia SP/SADT](#tela-18) | Menu corrigido e aceito; formulário em revisão | Logo e menu restaurados. Marcação de obrigatoriedade e dados do contratado solicitante ainda precisam de revisão. |
| [19. Dados complementares SP/SADT](#tela-19) | Última prévia; revisão pendente | Executante/CNES condicionais; indicador de recém-nato obrigatório no envio. Sem aprovação visual explícita após a apresentação. |

## Galeria
<a id="tela-01"></a>

### 1. Login

Direção visual aprovada. Entrada de funcionários; recuperação ainda requer telas próprias.

![Login — prévia conceitual com dados fictícios](images/01-login.png)

<a id="tela-02"></a>

### 2. Visão geral da gestão

Referência visual aprovada. Indicadores fictícios; visão ampla não representa módulos implementados.

![Visão geral da gestão — prévia conceitual com dados fictícios](images/02-visao-geral-gestao.png)

<a id="tela-03"></a>

### 3. Equipe

Prévia aprovada no fluxo. Gestão de acessos pela TI; suspensão não pertence à recepção.

![Equipe — prévia conceitual com dados fictícios](images/03-equipe.png)

<a id="tela-04"></a>

### 4. Convidar funcionário

Prévia aprovada no fluxo. Perfis e setores em pares explícitos.

![Convidar funcionário — prévia conceitual com dados fictícios](images/04-convidar-funcionario.png)

<a id="tela-05"></a>

### 5. Aceitar convite

Versão revista. Removido o link “Já tenho conta no Ordia”; a regra de conta existente permanece no fluxo de acesso.

![Aceitar convite — prévia conceitual com dados fictícios](images/05-aceitar-convite.png)

<a id="tela-06"></a>

### 6. Painel da recepção

Prévia aprovada no fluxo. Recepção solicita cancelamento e acompanha, sem executá-lo.

![Painel da recepção — prévia conceitual com dados fictícios](images/06-painel-recepcao.png)

<a id="tela-07"></a>

### 7. Solicitações de cancelamento

Fluxo aprovado; vocabulário a revisar. A coluna “Guia” nesta imagem representa atendimento interno; não é cancelamento TISS. Identificadores G precisam ser alinhados.

![Solicitações de cancelamento — prévia conceitual com dados fictícios](images/07-solicitacoes-cancelamento.png)

<a id="tela-08"></a>

### 8. Cadastrar paciente

Prévia aprovada no fluxo. CPF quando existente; alternativa documental e ao menos um contato precisam estar claros na validação final.

![Cadastrar paciente — prévia conceitual com dados fictícios](images/08-cadastrar-paciente.png)

<a id="tela-09"></a>

### 9. Possível duplicidade

Prévia aprovada no fluxo. Conferência humana; sem mesclagem automática de pessoas.

![Possível duplicidade — prévia conceitual com dados fictícios](images/09-possivel-duplicidade.png)

<a id="tela-10"></a>

### 10. Cadastro provisório

Prévia aprovada no fluxo. Identidade pendente e número interno; regularização com histórico ainda a detalhar.

![Cadastro provisório — prévia conceitual com dados fictícios](images/10-cadastro-provisorio.png)

<a id="tela-11"></a>

### 11. Lista de pacientes

Prévia aprovada no fluxo. Busca e situações cadastrais; não concede arquivamento à recepção.

![Lista de pacientes — prévia conceitual com dados fictícios](images/11-lista-pacientes.png)

<a id="tela-12"></a>

### 12. Ficha do paciente

Prévia aprovada; vocabulário a revisar. Histórico usa “Guia”/“Abrir guia” para atendimento interno. Corrigir para atendimento na revisão.

![Ficha do paciente — prévia conceitual com dados fictícios](images/12-ficha-paciente.png)

<a id="tela-13"></a>

### 13. Novo atendimento

Versão revista orientada a TISS. Regime separado de caráter. “A confirmar” é estado interno. Não equivale a elegibilidade.

![Novo atendimento — prévia conceitual com dados fictícios](images/13-novo-atendimento.png)

<a id="tela-14"></a>

### 14. Resumo do atendimento

Versão revista. Sem linha Setor no cartão; médico responsável pode aguardar atribuição.

![Resumo do atendimento — prévia conceitual com dados fictícios](images/14-resumo-atendimento.png)

<a id="tela-15"></a>

### 15. Dados do convênio

Prévia discutida. Elegibilidade ainda não consultada; presença e validade têm regras próprias. Rascunho não equivale a mensagem validada.

![Dados do convênio — prévia conceitual com dados fictícios](images/15-dados-convenio.png)

<a id="tela-16"></a>

### 16. Guias e autorizações

Prévia aprovada no fluxo. Estado vazio; preparar guia não significa transmitir ou autorizar.

![Guias e autorizações — prévia conceitual com dados fictícios](images/16-guias-autorizacoes.png)

<a id="tela-17"></a>

### 17. Definir médico responsável

Prévia aprovada no fluxo. Registros profissionais demonstrativos; responsável não é automaticamente solicitante.

![Definir médico responsável — prévia conceitual com dados fictícios](images/17-definir-medico.png)

<a id="tela-18"></a>

### 18. Preparar guia SP/SADT

Menu corrigido e aceito; formulário em revisão. Logo e menu restaurados. Marcação de obrigatoriedade e dados do contratado solicitante ainda precisam de revisão.

![Preparar guia SP/SADT — prévia conceitual com dados fictícios](images/18-preparar-guia-spsadt.png)

<a id="tela-19"></a>

### 19. Dados complementares SP/SADT

Última prévia; revisão pendente. Executante/CNES condicionais; indicador de recém-nato obrigatório no envio. Sem aprovação visual explícita após a apresentação.

![Dados complementares SP/SADT — prévia conceitual com dados fictícios](images/19-dados-complementares.png)

## Controle dos arquivos
O [manifesto](manifest.json) identifica o arquivo de origem, tamanho, SHA-256 e hash do objeto Git de cada imagem. Os PNGs preservam os arquivos apresentados, sem recompressão ou alteração silenciosa. Iterações descartadas de logo/menu não fazem parte da galeria.

## O que falta
- Revisar a última prévia e os campos normativos da SP/SADT.
- Corrigir os rótulos Guia/Atendimento nas telas antigas e as marcações de obrigatoriedade.
- Completar protótipos dos demais fluxos selecionados, sem considerar concluída a etapa 15.
- Revisar responsividade, teclado, foco, contraste, mensagens e cenários de falha.
- Confrontar os protótipos com o código e montar o plano de implementação.

Veja o [progresso do roteiro](../product/planning-progress.md) e o [estado do código](../product/implementation-status.md).

