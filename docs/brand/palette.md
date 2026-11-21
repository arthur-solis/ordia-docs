# Paleta e direção visual do ORDIA

## Decisão aprovada
Em 05/11/2026, o autor aprovou como base da paleta a segunda prévia do painel, criada a partir da referência oficial da marca **Conceito Fusão** em `ordia-application/docs/images/imagens.md`.

A direção aprovada combina **azul profundo, azul tecnológico e turquesa**, com fundos claros e textos escuros. A aprovação define a família cromática e a linguagem geral; não define ainda códigos HEX/RGB, tipografia ou medidas finais.

## Prévia visual aprovada
![Prévia conceitual do painel ORDIA com a direção cromática aprovada e dados fictícios](ordia-painel-paleta-aprovada.png)

A imagem gerada ilustra a direção aprovada. Não é arquivo mestre da logo nem definição exata de cores.

## Papéis das cores
| Família | Uso de referência |
|---|---|
| Azul profundo | Menu lateral, estrutura da navegação e fundo escuro para aplicação da marca |
| Azul tecnológico | Ações principais e destaques de interação |
| Turquesa | Acentos da identidade, indicadores e destaques complementares |
| Branco e cinza claro | Área de trabalho, painéis e fundos de formulários/tabelas |
| Azul muito escuro/cinza escuro | Textos principais com leitura clara |

Esses papéis orientam os protótipos. A atribuição final a cada componente será consolidada e verificada antes da implementação visual.

## Marca e referência
A referência oficial está no [arquivo de imagens da aplicação](https://github.com/arthur-solis/ordia-application/blob/main/docs/images/imagens.md), no bloco **Conceito Fusão / Sistema Integrado**. O acesso a esse arquivo depende de permissão no repositório privado.

O símbolo combina núcleo, órbitas e eixo central, acompanhado do wordmark ORDIA. A prévia gerada é uma exploração visual: a implementação deverá usar o arquivo original da marca, preservando proporções e formas.
Não substituir o símbolo por uma órbita genérica nem usar outras alternativas do quadro de conceitos como se fossem a marca aprovada.

## Interface de referência
- Menu lateral escuro e área de trabalho clara.
- Painéis brancos, bordas discretas e cantos levemente arredondados.
- Hierarquia legível em formulários, tabelas e indicadores.
- Ícones acompanhados de texto nas ações importantes.
- Estados informados também por texto ou ícone, sem depender exclusivamente de cor.
- Dados e nomes do painel de referência são fictícios; a imagem não comprova implementação dos módulos apresentados.

## Pendências para consolidar os tokens
1. Definir valores HEX/RGB para as cores da marca e os neutros; os tons da imagem gerada são aproximações.
2. Definir variações de interação: repouso, hover, foco, seleção e desabilitado.
3. Definir cores semânticas para sucesso, aviso, erro e informação, sem confundi-las com a identidade da marca.
4. Verificar contraste dos pares usados em texto, controles e foco.
5. Definir tipografia, escala de espaçamento, bordas e componentes.
6. Documentar tratamento específico de classificação de risco quando o protocolo correspondente for definido; não deduzir cores clínicas a partir da paleta de marca.

## Estado
**Base cromática e direção visual aprovadas.** Tokens completos, componentes e validação de acessibilidade permanecem pendentes. Nenhuma alteração no frontend é realizada por este registro.

## Documento relacionado
- [Diretrizes da marca](README.md)
