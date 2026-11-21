# Roteiro do TCC · Progresso
Atualizado em 20/11/2026 a partir das decisões desta etapa. Um encontro pode cobrir mais de um assunto; passagem de dias não conclui tarefas.

**14 etapas discutidas e aprovadas no planejamento; prototipação antecipada pausada; conferência inicial do código realizada.** Isso não significa 14 módulos implementados ou documentação final de todos os detalhes. A base de código e suas limitações estão em [estado de implementação](implementation-status.md).

| Etapa | Foco | Situação e resultado |
|---|---|---|
| 1 | Escopo do TCC | Direção inicial aprovada: hospital geral privado, convênios/particulares; recorte demonstrável final ainda a priorizar |
| 2 | Perfis de usuário | Funcionários; portal de paciente fora do cenário inicial |
| 3 | Mapa de telas | Mapa hospitalar inicial aprovado |
| 4 | Navegação | Ambiente único, áreas conforme permissões e contexto |
| 5 | Identidade visual | Família visual aprovada; tokens finais e biblioteca de componentes a fechar |
| 6 | Acesso | Operador cria tenant e convida primeira TI; TI convida funcionários |
| 7 | Pacientes | Ficha única, CPF quando existente, cadastro provisório e regularização planejada |
| 8 | Profissionais e recursos | Recursos compartilhados e reservas autorizadas por setor |
| 9 | Agenda | Disponibilidade, conflitos, remarcação e histórico |
| 10 | Equipe e permissões | Perfis com setores pareados; ações restritas atualizadas na etapa 14 |
| 11 | Documentos e arquivos | Produção interna e anexos externos; catálogo por módulo a detalhar |
| 12 | Relatórios e auditoria | Filtros/exportações e rastreamento de acessos sensíveis |
| 13 | Configurações e visão geral | Definição inicial aprovada, ajustável após validar os fluxos |
| 14 | Comportamentos comuns | Estados de tela, confirmações, conflitos e responsabilidades |
| 15 | Protótipos | **Pausada por decisão do autor:** base suficiente para iniciar; novas telas conforme implementação |
| 16 | Responsividade e acessibilidade | Incorporar ao aceite de cada módulo; não concluída globalmente |
| 17 | Revisão dos fluxos | Executar por módulo; permanecem fluxos e detalhes pendentes |
| 18 | Conferência do código existente | Conferência inicial da main concluída; execução local e branches fora do escopo |
| 19 | Ambiente local com dados fictícios | Pendente de validação reproduzível |
| 20 | Plano de implementação por módulo | Plano inicial registrado; nenhum item implementado por esta atualização |

## Ponto de retomada
**Começar pelo ambiente local com dados fictícios e pelas pendências técnicas confirmadas.** Depois adaptar estrutura visual/acesso, equipe/permissões e pacientes, nessa ordem. O [plano de adequação do código](implementation-backlog.md) detalha evidências, prioridades e critérios de aceite.

Após a primeira galeria, o chat refinou as seções da SP/SADT, o rascunho salvo, exportação PDF, documentos administrativos, histórico e solicitação/acompanhamento de cancelamento. A [galeria](../prototypes/README.md) publicada ainda é o conjunto de 19 imagens; nem todas as revisões posteriores estão incorporadas aos arquivos do repositório. O PDF de duas páginas é um exemplo separado, sem gerador equivalente na aplicação.

O autor decidiu interromper a criação antecipada de telas e produzi-las conforme o desenvolvimento dos módulos. Não é necessário terminar todos os protótipos para iniciar o código. Não considerar responsividade, acessibilidade ou fluxos restantes concluídos apenas pela mudança de ordem.

## Regras mantidas
- Hospedagem e serviços de produção ficam para depois do TCC.
- Demonstração com hospital e pessoas fictícias.
- Acesso somente por funcionários.
- Aprovar imagem ou regra não equivale a alterar código.
- Não executar merges automaticamente por causa do roteiro ou de lembretes.
- Os protótipos orientados a TISS não provam transmissão, elegibilidade ou autorização reais.

## Documentação complementar
- [Documentos e arquivos](hospital-documents.md)
- [Relatórios e auditoria](hospital-reports-audit.md)
- [Configurações e painel](hospital-settings-dashboard.md)
- [Comportamentos comuns e cancelamentos](hospital-interface-behavior.md)
- [Atendimento e TISS](hospital-attendance-tiss.md)

