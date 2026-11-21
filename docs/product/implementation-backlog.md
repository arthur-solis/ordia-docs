# Plano de adequação do código ao planejamento hospitalar
Revisão: 20/11/2026. Referência conferida: main de ordia-application, commit `648efa574ba751605b1f4cab1426bbd000877ee3`. Situação inicial de todos os itens abaixo: **pendente de implementação ou validação**, salvo a conferência estática explicitamente registrada.

## Direção aprovada
Pausar a produção antecipada de telas. Utilizar a base visual existente e criar as próximas telas conforme cada módulo for implementado. Responsividade, acessibilidade, estados de erro e revisão do fluxo entram no critério de conclusão de cada módulo. A pausa não conclui os protótipos restantes.

Esta revisão compara código com decisões posteriores; não afirma que toda diferença era defeito do MVP anterior. Não altera o código, não faz merge e não comprova execução local.

## Base que será reaproveitada
Identidade e sessões, recuperação de senha, vínculos/convites, autorização por instituição, pacientes básicos, recursos/disponibilidade, agenda, anexos privados, auditoria e exportações genéricas. A existência da base não comprova os novos fluxos hospitalares.

## Pendências técnicas anteriores ao desenvolvimento funcional
| ID | Prioridade | Evidência confirmada | Correção e critério de conclusão |
|---|---|---|---|
| TEC-01 | Alta | Auditoria de dependências falhou ao consultar NVD por chave ausente/inválida. Upload de artefatos também falhou por quota. | Corrigir configuração e retenção/quota; executar auditoria completa e revisar seus resultados. Não interpretar falha de análise como vulnerabilidade confirmada nem como ausência de vulnerabilidades. |
| TEC-02 | Alta | Ambiente local não foi executado nesta revisão. Compose padrão sobe apenas MySQL; SMTP e antimalware precisam de configuração própria. | Documentar e validar execução de frontend/backend/banco, e-mail capturado localmente e antimalware; hospital, primeira TI e dados fictícios reproduzíveis. Manter verificações de segurança. |

Evidência TEC-01: [execução 43951844965](https://github.com/arthur-solis/ordia-application/actions/runs/43951844965), etapa de análise: `Invalid API Key, length of 0`; etapa de upload: `Artifact storage quota has been hit`. A revisão não consultou valores de segredos nem concluiu uma auditoria atual de vulnerabilidades.
Evidência TEC-02: [docker-compose.yml, linha 1](https://github.com/arthur-solis/ordia-application/blob/648efa574ba751605b1f4cab1426bbd000877ee3/docker-compose.yml#L1).

## Diferenças confirmadas e trabalho por módulo
| ID | Prioridade | Estado no código conferido | Mudança necessária | Aceite mínimo |
|---|---|---|---|---|
| IMP-01 | Alta | Tema verde e navegação centralizada na página principal | Aplicar marca/paleta/menu aprovados e separar componentes e fluxos conforme necessidade real | Login e estrutura principal consistentes; navegação preserva autorização, teclado e adaptação de tela |
| IMP-02 | Alta | Cadastro de instituição cria usuário e senha do administrador | Operador provisiona hospital e convida primeira TI; retirar cadastro público desse fluxo | Primeiro administrador define sua senha pelo convite; funcionário não cria hospital pelo login |
| IMP-03 | Alta | Perfis por instituição, sem setor; recepção tem cancelamento direto de agenda | Modelar setores e pares perfil–setor; atualizar permissões e autorização no servidor | Recepção solicita; Gestão de contas cancela agenda/arquiva paciente; TI suspende vínculo; negar acessos cruzados e links diretos indevidos |
| IMP-04 | Alta | Documento opcional CPF/CNPJ; busca por nome; nascimento e contato obrigatórios | Implementar cadastro normal aprovado, CPF quando existente, documento alternativo, número interno e busca; cadastro provisório e regularização | Cadastro provisório não exige dados desconhecidos; duplicidade exige conferência; regularização preserva histórico e isolamento |
| IMP-05 | Alta | Agenda armazena agendamentos; não há entidade independente de atendimento hospitalar | Criar registro de atendimento ligado ao paciente e, quando houver, ao agendamento; regime, caráter, responsável e contexto | Entrada espontânea possível; números distintos de paciente/atendimento/guia; responsável não é automaticamente solicitante |
| IMP-06 | Alta | Transição de cancelamento de agendamento é direta; sem pedido de análise | Implementar solicitação interna, justificativa, acompanhamento e decisão por Gestão de contas | Pedido não cancela automaticamente; análise possível com registros assistenciais; decisão autorizada preserva documentos e histórico |
| IMP-07 | Média | Nenhum módulo de elegibilidade/SP-SADT encontrado no backend conferido | Modelar convênio no atendimento, solicitação profissional, rascunho de guia, itens e validações por mensagem ANS | Rascunho incompleto permitido; nenhuma elegibilidade/autorização positiva sem resposta; transmissão real tem especificação e testes próprios |
| IMP-08 | Média | Anexos ligados a paciente ou agendamento; inspeção síncrona antes da gravação | Incluir vínculo ao atendimento, categorias, origem, versão, autor e acesso por categoria/contexto; definir ciclo de verificação | Visualização/download autorizados; indisponibilidade enquanto em verificação se adotado esse fluxo; nova versão não apaga a anterior |
| IMP-09 | Média | Exportador gera relatórios genéricos em PDF/CSV | Implementar PDF de conferência SP/SADT e saída padronizada separada, com dados e versões do registro | Rascunho identificado, sem fabricar senha/resposta; snapshot/versionamento; impressão revisada; nenhuma declaração automática de conformidade |
| IMP-10 | Média | Auditoria transacional genérica, sem histórico específico do atendimento | Criar consulta administrativa do atendimento e ampliar eventos de acesso conforme requisitos | Recepção vê somente detalhes autorizados; registros preservados; sem conteúdo clínico ou segredos indevidamente expostos |

## Evidências de código
Os links apontam para o commit conferido; o repositório da aplicação é privado e exige acesso. Esta página não publica seu código.
- IMP-01: [interface, linha 70](https://github.com/arthur-solis/ordia-application/blob/648efa574ba751605b1f4cab1426bbd000877ee3/frontend/src/routes/%2Bpage.svelte#L70); [tema, linha 1](https://github.com/arthur-solis/ordia-application/blob/648efa574ba751605b1f4cab1426bbd000877ee3/frontend/src/style.css#L1).
- IMP-02: [criação do tenant, linha 62](https://github.com/arthur-solis/ordia-application/blob/648efa574ba751605b1f4cab1426bbd000877ee3/backend/src/main/java/br/com/ordia/identity/application/AuthenticationService.java#L62); [cadastro no login, linha 40](https://github.com/arthur-solis/ordia-application/blob/648efa574ba751605b1f4cab1426bbd000877ee3/frontend/src/lib/Auth.svelte#L40).
- IMP-03: [atribuição de perfis, linha 31](https://github.com/arthur-solis/ordia-application/blob/648efa574ba751605b1f4cab1426bbd000877ee3/backend/src/main/java/br/com/ordia/tenancy/MembershipService.java#L31); [autorização por instituição, linha 10](https://github.com/arthur-solis/ordia-application/blob/648efa574ba751605b1f4cab1426bbd000877ee3/backend/src/main/java/br/com/ordia/shared/security/DomainAccess.java#L10); [recepção cancela agenda, linha 94](https://github.com/arthur-solis/ordia-application/blob/648efa574ba751605b1f4cab1426bbd000877ee3/backend/src/main/resources/db/migration/V003__seed_mvp_roles_and_permissions.sql#L94).
- IMP-04: [validação do paciente, linha 15](https://github.com/arthur-solis/ordia-application/blob/648efa574ba751605b1f4cab1426bbd000877ee3/backend/src/main/java/br/com/ordia/patients/PatientService.java#L15); [busca, linha 37](https://github.com/arthur-solis/ordia-application/blob/648efa574ba751605b1f4cab1426bbd000877ee3/backend/src/main/java/br/com/ordia/patients/PatientService.java#L37); [schema, linha 1](https://github.com/arthur-solis/ordia-application/blob/648efa574ba751605b1f4cab1426bbd000877ee3/backend/src/main/resources/db/migration/V007__patients_resources_and_appointments.sql#L1).
- IMP-05/06: [agendamentos, linha 39](https://github.com/arthur-solis/ordia-application/blob/648efa574ba751605b1f4cab1426bbd000877ee3/backend/src/main/resources/db/migration/V007__patients_resources_and_appointments.sql#L39); [transições, linha 115](https://github.com/arthur-solis/ordia-application/blob/648efa574ba751605b1f4cab1426bbd000877ee3/backend/src/main/java/br/com/ordia/scheduling/AppointmentService.java#L115).
- IMP-07: conferência do inventário de arquivos, controladores, serviços e migrations do backend no commit indicado; ausência no escopo examinado, sem alegação sobre branches não revisadas.
- IMP-08: [vínculos de arquivo, linha 15](https://github.com/arthur-solis/ordia-application/blob/648efa574ba751605b1f4cab1426bbd000877ee3/backend/src/main/java/br/com/ordia/files/FileService.java#L15); [inspeção antes da gravação, linha 44](https://github.com/arthur-solis/ordia-application/blob/648efa574ba751605b1f4cab1426bbd000877ee3/backend/src/main/java/br/com/ordia/files/FileService.java#L44).
- IMP-09: [geração atual de PDF, linha 15](https://github.com/arthur-solis/ordia-application/blob/648efa574ba751605b1f4cab1426bbd000877ee3/backend/src/main/java/br/com/ordia/reports/ExportRenderer.java#L15).
- IMP-10: [registro de auditoria, linha 13](https://github.com/arthur-solis/ordia-application/blob/648efa574ba751605b1f4cab1426bbd000877ee3/backend/src/main/java/br/com/ordia/shared/audit/AuditService.java#L13).

## Ordem de execução
1. Resolver TEC-01 e validar TEC-02: ambiente local, dados fictícios e diagnóstico de dependências.
2. IMP-01 e IMP-02: estrutura visual e acesso, reaproveitando autenticação e convites.
3. IMP-03: setores, perfis e permissões antes dos novos fluxos.
4. IMP-04: pacientes, cadastro normal/provisório e identificação.
5. IMP-05 e IMP-06: atendimento e pedido de cancelamento.
6. IMP-07, IMP-08 e IMP-09: guias, documentos e PDF, em incrementos.
7. IMP-10: histórico do atendimento; os eventos necessários devem ser implementados junto de cada operação desde os incrementos anteriores.

As prioridades são para adequação ao TCC, não promessa de implantação. A integração externa com operadora será tratada separadamente; uma simulação deve ser identificada como simulação.

## Evidência de testes e limites
No commit indicado, [backend](https://github.com/arthur-solis/ordia-application/actions/runs/41371729668) registrou 15 testes unitários e 33 de integração aprovados; [frontend](https://github.com/arthur-solis/ordia-application/actions/runs/41371729703) registrou verificação de tipos, build e 5 testes aprovados. São execuções históricas desse commit, não testes novos desta revisão. A auditoria de dependências posterior não concluiu.

Nenhum teste local ou alteração de código foi realizado nesta conferência. Branches de implementação não foram integralmente revisadas; resultados se referem à main fixada. Antes de implementar, conferir novamente o estado remoto e preservar alterações locais existentes.

## Critério de conclusão por módulo
Regra e contrato coerentes, autorização no servidor, testes relevantes, fluxo visual revisado com estados de erro, responsividade/acessibilidade e documentação atualizada. Criar apenas as telas necessárias ao incremento em execução.
