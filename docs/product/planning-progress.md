# Roteiro do TCC · Progresso
Atualizado em 19/11/2026 a partir das decisões desta etapa. Um encontro pode cobrir mais de um assunto; passagem de dias não conclui tarefas.

**14 etapas discutidas e aprovadas no planejamento; etapa 15 em andamento.** Isso não significa 14 módulos implementados ou documentação final de todos os detalhes. A base de código e suas limitações estão em [estado de implementação](implementation-status.md).

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
| 15 | Protótipos | **Em andamento:** acesso, equipe, recepção, pacientes e atendimento/convênio/SP-SADT |
| 16 | Responsividade e acessibilidade | Pendente |
| 17 | Revisão dos fluxos | Pendente; já há ajustes identificados no inventário |
| 18 | Conferência do código existente | Pendente; comparar regras atuais com o código, sem presumir implementação |
| 19 | Ambiente local com dados fictícios | Pendente de validação reproduzível |
| 20 | Plano de implementação por módulo | Pendente |

## Ponto de retomada
Última prévia apresentada: **Dados complementares da guia SP/SADT**. Está registrada para revisão, sem aprovação visual explícita posterior. A próxima atividade é revisar essa prévia e as pendências normativas do formulário antes de seguir com outros estados do fluxo.

A [galeria de protótipos](../prototypes/README.md) identifica telas, versões e ressalvas. O planejamento preserva o ritmo de uma atividade pequena por encontro.

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

