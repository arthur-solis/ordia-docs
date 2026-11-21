# ADR-0003 · Prioridade do TCC e stack da base integrada

- Estado: adotado para a etapa acadêmica em 01/11/2026; parcialmente substituído pelo [ADR-0004](ADR-0004-hospital-scope-navigation.md) quanto à exclusão do financeiro da visão do produto. Prioridade do TCC e decisões técnicas permanecem.
- Contexto: o Documento Mestre ainda apresentava tecnologias previstas inicialmente e requisitos de operação externa como se fossem necessários para a entrega atual. O núcleo e a interface já foram integrados à main.
- Decisão: priorizar implementação, revisão, testes, documentação e demonstração local do TCC, com dados fictícios. Hospedagem pública, provedores externos e operação com usuários reais serão avaliados após o TCC.
- Frontend atual: SvelteKit, Svelte, TypeScript e CSS próprio responsivo. Tailwind CSS não foi adotado na base integrada; não é necessário introduzi-lo apenas para cumprir a previsão antiga.
- Estado compartilhado: sessões e limites de tentativas usam MySQL. Redis é uma possibilidade futura condicionada a necessidade comprovada.
- Conteúdo privado: permanece criptografado no MySQL conforme [ADR-0002](ADR-0002-private-content-mvp.md). Object storage privado é evolução futura.
- Identidade: autenticação própria da aplicação. Recuperação e convites podem usar captura SMTP local na demonstração; a configuração e os links ainda precisam ser documentados e validados. Esta decisão não implementa um modo local nem autoriza expor tokens em logs.
- Consequências: a conclusão do TCC não depende de contratar serviços. Permanecem obrigatórias validação, autorização, isolamento entre instituições e proteção de arquivos. O ambiente local de arquivos ainda precisa de chave e antimalware configurados.
- Pendências acadêmicas: detalhamento e revisão das telas, estados e navegação; execução local reproduzível; roteiro de apresentação e evidências. Código integrado não significa aprovação visual nem conclusão do TCC.
- Limite original da base integrada: financeiro, notificações gerais, integrações externas de negócio e funções globais de administração da plataforma. O ADR-0004 inclui financeiro/faturamento na visão hospitalar; implementação e recorte do TCC serão definidos por etapas.
- Referências: [MVP](../product/mvp.md), [estado de implementação](../product/implementation-status.md) e [Documento Mestre](../master/documento-mestre.md).
