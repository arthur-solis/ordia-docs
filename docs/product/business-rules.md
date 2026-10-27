# Regras de Negócio

Regras de negócio detalhadas do ORDIA, derivadas dos requisitos funcionais, casos de uso, MVP e modelo de domínio.

## Como ler este documento

Cada regra possui um identificador estável, uma classificação e critérios verificáveis. As escolhas fechadas para o MVP estão em [Decisões do MVP](mvp-decisions.md) e complementam as regras classificadas originalmente como decisão pendente para os fluxos do MVP. Regras classificadas como **Definida** orientam implementação e testes. Itens **Decisão pendente** não devem ser fixados em código como política definitiva sem validação. Itens **Futuro** e **Fora do MVP** não bloqueiam o núcleo do primeiro produto.

| Classificação | Significado |
|---|---|
| Definida | Regra aprovada para o escopo atual; deve ser implementada e testada quando o domínio entrar em desenvolvimento. |
| Decisão pendente | Direção conhecida, mas há escolha de produto, segurança ou operação a confirmar. |
| Futuro | Capacidade prevista, mas não necessária para o MVP. |
| Fora do MVP | Capacidade explicitamente excluída do primeiro incremento. |

## 1. Identity & Access

### 1.1 Princípio de separação

> **Autenticação identifica quem é o usuário. Membership determina em qual organização ele pode operar. Role e Permission determinam o que ele pode fazer.**

```text
User
  └── Membership
        └── Tenant
              └── Role
                    └── Permission
```

### 1.2 Regras

| ID | Regra | Classificação | Critérios verificáveis |
|---|---|---|---|
| BR-IAM-001 | Todo acesso a recurso protegido exige uma identidade autenticada válida. | Definida | Uma requisição sem credencial válida para recurso protegido é negada antes da execução do caso de uso. |
| BR-IAM-002 | `User` é uma identidade global da plataforma e não representa, por si só, autorização em uma organização. | Definida | A existência de um usuário sem Membership não permite ler, criar, alterar ou excluir recurso tenant-owned. |
| BR-IAM-003 | Um mesmo User pode possuir Memberships em mais de um Tenant, com papéis e permissões independentes em cada vínculo. | Definida | Alterar papel ou estado de um Membership não altera Memberships do mesmo User em outros Tenants. |
| BR-IAM-004 | O estado global inicial de um User deve ser `ACTIVE` ou `DISABLED`; somente User `ACTIVE` pode iniciar ou continuar operação autenticada. | Definida | Login e operações autenticadas de User `DISABLED` são negados; User `ACTIVE` ainda depende de credenciais, Membership e autorização válidos. |
| BR-IAM-005 | Um Membership deve possuir um dos estados `PENDING`, `ACTIVE`, `SUSPENDED` ou `REVOKED`. | Definida | Não é permitido persistir estado fora do catálogo; a transição deve ser validada no backend. |
| BR-IAM-006 | Apenas Membership `ACTIVE` permite operar no Tenant correspondente. | Definida | Requisição com Membership `PENDING`, `SUSPENDED` ou `REVOKED` não acessa recursos daquele Tenant, mesmo quando o token ou URL referencia o Tenant. |
| BR-IAM-007 | O Tenant Context deve ser resolvido e validado pelo backend a partir de fonte confiável. Um `tenant_id` fornecido pelo cliente não é autorização suficiente. | Definida | Alterar `tenant_id`, ID de recurso, filtro ou rota no cliente não concede acesso a outro Tenant. |
| BR-IAM-008 | A autorização de recurso tenant-owned deve validar, nesta ordem lógica: autenticação, Tenant Context, Membership ativo, permissão e escopo do recurso. | Definida | Um usuário autenticado, mas sem Membership ativo ou permissão, recebe negação antes de obter dados ou executar alteração. |
| BR-IAM-009 | A autorização definitiva ocorre no backend. Controles de interface servem somente à experiência do usuário. | Definida | Chamar diretamente uma API que corresponde a botão ou rota ocultos no frontend continua exigindo a mesma permissão no backend. |
| BR-IAM-010 | O modelo inicial de acesso é RBAC: Role agrupa Permissions atribuídas no contexto do Membership. | Definida | A decisão de acesso é derivada das permissões efetivas do Membership no Tenant atual, e não de uma role global do User. |
| BR-IAM-011 | O catálogo inicial de roles é `TENANT_ADMIN`, `MANAGER`, `PROFESSIONAL`, `RECEPTION`, `FINANCE` e `AUDITOR`; a lista e a matriz final de Permissions ainda requerem validação por domínio. | Decisão pendente | Nenhum endpoint novo pode depender de uma permissão implícita; a role e as Permissions exigidas devem ser documentadas antes da implementação. |
| BR-IAM-012 | Permissões representam capacidades concretas e podem ser limitadas por escopo de Tenant e, futuramente, unidade, recurso, proprietário ou função operacional. | Futuro | Quando escopos adicionais forem adotados, testes devem provar que uma permissão fora do escopo não concede acesso. |
| BR-IAM-013 | A autenticação por senha deve validar credenciais sem armazenar ou registrar senhas em texto puro. | Definida | Senhas e tokens completos não aparecem em logs, respostas de erro, auditoria ou telemetria; o armazenamento usa hash apropriado para senha. |
| BR-IAM-014 | Uma tentativa de login inválida não deve revelar se o identificador da conta existe, está ativo ou possui Membership. | Definida | Credencial incorreta, usuário inexistente e usuário indisponível produzem resposta pública equivalente, sem dados de conta ou Tenant. |
| BR-IAM-015 | Falhas de login devem ser registradas para segurança sem registrar senha, token ou dado sensível desnecessário. | Definida | Cada falha gera evento com resultado, data/hora e contexto técnico mínimo; nenhum segredo é armazenado. |
| BR-IAM-016 | Limites de tentativas, duração de bloqueio, CAPTCHA e rate limiting para login e recuperação de senha devem ser definidos antes da implementação de produção. | Decisão pendente | A política escolhida deve declarar limiar, janela, duração, desbloqueio e resposta ao cliente, com testes de abuso. |
| BR-IAM-017 | A sessão de API utiliza JWT de curta duração e credencial de renovação controlada; tokens expirados, inválidos, malformados ou sem claims obrigatórias são rejeitados. | Definida | Um access token fora da validade, com assinatura inválida, formato inválido ou identidade não validável não autoriza nenhuma operação. |
| BR-IAM-018 | JWT não é a fonte definitiva de autorização. Em operações protegidas, o backend deve considerar o estado atual de User, Membership, Tenant e permissões aplicáveis. | Definida | Desativar User, suspender/revogar Membership ou remover permissão bloqueia operações subsequentes conforme a estratégia de revogação adotada. |
| BR-IAM-019 | Claims de token devem conter apenas o mínimo necessário, incluindo identidade, emissão, expiração e identificador do token; Tenant, roles e permissions somente quando necessários à estratégia aprovada. | Definida | Nenhum JWT contém senha, dado clínico, segredo ou informação pessoal além do necessário para autenticação/autorização. |
| BR-IAM-020 | O método de encerramento de sessão e a revogação antecipada de access/refresh tokens devem ser definidos para suportar logout, desativação e incidente de segurança. | Decisão pendente | A decisão deve cobrir invalidação de refresh token, rotação, detecção de reutilização e efeito sobre tokens emitidos antes da mudança. |
| BR-IAM-021 | A recuperação de senha deve usar fluxo de uso único, validade limitada, confirmação segura e resposta pública não enumerável. | Definida | Solicitar recuperação para identificador existente ou inexistente retorna resposta pública equivalente; token usado, expirado ou inválido não permite redefinição. |
| BR-IAM-022 | A validade, canal de entrega, limites de solicitação e revalidação após recuperação de senha devem ser definidos antes da implementação de produção. | Decisão pendente | A política aprovada documenta expiração, limitação, invalidação de sessões e exigência de auditoria. |
| BR-IAM-023 | Desativar um User impede novos logins e o prosseguimento de operações autenticadas; o histórico de domínio e auditoria não é apagado por essa ação. | Definida | Após a desativação, novo login é negado e requisições subsequentes são bloqueadas segundo a estratégia de revogação; registros históricos permanecem consultáveis apenas por quem tiver autorização. |
| BR-IAM-024 | Suspender ou revogar um Membership impede acesso somente ao Tenant daquele vínculo, sem desativar automaticamente o User ou seus demais Memberships. | Definida | Um usuário com Membership revogado no Tenant A e ativo no Tenant B não acessa A, mas pode operar em B conforme suas permissões. |
| BR-IAM-025 | A exclusão física de User, anonimização e políticas de retenção de identidade devem ser definidas com avaliação de privacidade, auditoria e requisitos legais. | Fora do MVP | Nenhuma implementação do MVP exclui fisicamente User ou eventos de auditoria como mecanismo padrão de desativação. |
| BR-IAM-026 | Eventos relevantes de identidade e acesso devem gerar auditoria com ator quando conhecido, Tenant quando aplicável, data/hora, ação, resultado e metadados mínimos. | Definida | São auditáveis ao menos: login bem-sucedido ou falho, logout quando suportado, recuperação e alteração de senha, ativação/desativação de User, criação/alteração/suspensão/revogação de Membership e alteração de roles/permissões. |
| BR-IAM-027 | Auditoria não deve armazenar senha, token completo, segredo ou dados sensíveis que não sejam necessários à investigação. | Definida | Uma inspeção dos eventos de Identity & Access não encontra credenciais, tokens completos ou segredos. |
| BR-IAM-028 | O acesso a eventos de auditoria é restrito a usuários autorizados e respeita o Tenant Context; acesso administrativo transversal exige escopo explícito. | Definida | Um usuário comum não consulta auditoria; um usuário autorizado no Tenant A não consulta eventos do Tenant B sem capacidade de plataforma explicitamente definida. |

### 1.3 Transições de Membership

| Estado de origem | Transições permitidas | Observação |
|---|---|---|
| `PENDING` | `ACTIVE`, `REVOKED` | A ativação confirma o vínculo; a forma de convite é decisão do domínio Tenant & Organization. |
| `ACTIVE` | `SUSPENDED`, `REVOKED` | `SUSPENDED` é reversível; `REVOKED` encerra o vínculo operacional atual. |
| `SUSPENDED` | `ACTIVE`, `REVOKED` | A reativação exige autorização administrativa. |
| `REVOKED` | nenhuma | Novo acesso exige novo Membership, não reativação silenciosa. |

### 1.4 Casos de teste mínimos para o domínio

- Requisição protegida sem autenticação é negada.
- User ativo sem Membership não acessa recurso tenant-owned.
- User ativo com Membership não ativo não opera no Tenant.
- User com acesso ao Tenant A não obtém recurso do Tenant B por ID, filtro ou alteração de contexto no cliente.
- Role/Permission no Tenant A não concede capacidade no Tenant B.
- User desativado e Membership revogado não conseguem prosseguir após a alteração de estado.
- Login inválido não enumera contas e gera auditoria sem segredo.
- JWT expirado, inválido ou malformado é negado.
- Recuperação de senha não enumera contas; token é único e expira.
- Eventos de auditoria de Identity & Access respeitam autorização e escopo de Tenant.

## 2. Tenant & Organization

O Tenant representa a organização que utiliza o ORDIA. Ele é o limite operacional e lógico de seus recursos, configurações e Memberships.

### 2.1 Regras

| ID | Regra | Classificação | Critérios verificáveis |
|---|---|---|---|
| BR-TEN-001 | Cada organização cadastrada é representada por exatamente um Tenant, com identificador interno único e imutável. | Definida | Dois Tenants não compartilham identificador; alterações cadastrais não alteram o identificador. |
| BR-TEN-002 | Todo recurso tenant-owned pertence a exatamente um Tenant no contexto normal de operação. | Definida | Pacientes, agendamentos, configurações, arquivos e auditoria não são retornados nem alterados sem escopo de Tenant válido. |
| BR-TEN-003 | Um Tenant possui um dos estados `PENDING`, `ACTIVE`, `SUSPENDED` ou `CLOSED`. | Definida | Não é permitido persistir estado fora do catálogo; toda mudança é validada pelo backend. |
| BR-TEN-004 | Somente Tenant `ACTIVE` permite operações normais sobre seus recursos. | Definida | Um usuário não cria, altera nem consulta recursos operacionais em Tenant `PENDING`, `SUSPENDED` ou `CLOSED`. |
| BR-TEN-005 | A criação de Tenant deve criar ou vincular um administrador inicial com Membership `ACTIVE` e role `TENANT_ADMIN`. | Definida | Tenant recém-criado não fica operacional sem administrador ativo autorizado a configurar a organização e gerir membros. |
| BR-TEN-006 | Um Tenant `ACTIVE` deve manter ao menos um Membership `ACTIVE` com capacidade administrativa. | Definida | Remover, revogar, suspender ou rebaixar o último administrador ativo é negado, exceto em encerramento ou transferência administrativa explícita. |
| BR-TEN-007 | A transferência administrativa deve conceder a capacidade ao sucessor antes de removê-la do administrador anterior. | Definida | Não há estado intermediário em que Tenant ativo fica sem administrador autorizado. |
| BR-TEN-008 | Criar, alterar dados ou configurar Tenant exige autorização administrativa no contexto daquele Tenant. | Definida | User sem permissão administrativa não altera cadastro ou configuração, ainda que conheça o identificador. |
| BR-TEN-009 | Configurações pertencem exclusivamente ao Tenant e não podem vazar por consulta, cache, job ou exportação. | Definida | Consulta no Tenant A não retorna valores do B; cache possui namespace por Tenant. |
| BR-TEN-010 | Convite ou criação de vínculo produz Membership `PENDING` até que o fluxo aprovado de ativação termine. | Definida | Usuário convidado não opera antes de o Membership ser `ACTIVE`. |
| BR-TEN-011 | Canal de convite, validade, reenvio, cancelamento e aceitação devem ser definidos antes da produção. | Decisão pendente | A política aprovada especifica destinatário, expiração, prevenção de enumeração de contas e auditoria. |
| BR-TEN-012 | Criar, ativar, suspender, revogar Membership e mudar roles exige permissão administrativa no Tenant atual. | Definida | User sem capacidade correspondente não administra Memberships, localmente ou em outro Tenant. |
| BR-TEN-013 | Tenant não concede acesso a User globalmente `DISABLED`; reativação de User é responsabilidade de Identity & Access. | Definida | Ativar Membership de User desativado é negado; reativar User não reativa Membership automaticamente. |
| BR-TEN-014 | A troca de Tenant Context é permitida apenas para User com Membership `ACTIVE` no destino. | Definida | Pedido para Tenant sem Membership ativo é negado e mantém o contexto anterior. |
| BR-TEN-015 | Depois da troca de contexto, roles, permissions, escopo e dados acessíveis são recalculados para o Tenant de destino. | Definida | Permissão existente só no Tenant A não autoriza ação no Tenant B. |
| BR-TEN-016 | Dados, cache de autorização e resultados do Tenant anterior não podem ser reutilizados após troca de contexto. | Definida | A troca não permite visualizar lista, detalhe, arquivo ou configuração carregados no Tenant anterior. |
| BR-TEN-017 | O mecanismo de seleção e persistência do Tenant Context na sessão/token deve ser definido sem confiar em ID livremente informado pelo cliente. | Decisão pendente | A decisão descreve fonte confiável, validação por requisição, renovação e múltiplos Memberships. |
| BR-TEN-018 | Suspender Tenant bloqueia operações de usuários e administração interna, preservando dados e auditoria para investigação e reativação autorizada. | Definida | Endpoints tenant-owned negam acesso e alteração normal durante suspensão; dados não são apagados. |
| BR-TEN-019 | Encerrar Tenant altera seu estado para `CLOSED` e impede operações normais e novos Memberships. | Definida | Tenant fechado não aceita contexto, convite, ativação de Membership nem operação tenant-owned. |
| BR-TEN-020 | Reativação de Tenant suspenso e encerramento exigem capacidade explícita, justificativa auditável e política aprovada. | Decisão pendente | A política define quem autoriza, condições impeditivas e eventual período de carência. |
| BR-TEN-021 | Exclusão física, anonimização, exportação e retenção de dados após encerramento exigem política de privacidade, segurança e requisitos legais. | Fora do MVP | MVP usa suspensão ou encerramento lógico; não apaga em massa dados como comportamento padrão. |
| BR-TEN-022 | Unidades, filiais, departamentos e escopos internos não são equivalentes a Tenant e terão modelo próprio quando necessários. | Futuro | Identificador de unidade não substitui `tenant_id` nem permite burlar autorização. |
| BR-TEN-023 | Acesso de administrador da plataforma a dados de Tenant não é implícito; requer capacidade, finalidade e escopo definidos. | Definida | Role de plataforma sem autorização transversal documentada não consulta dados tenant-owned irrestritamente. |
| BR-TEN-024 | Eventos administrativos de Tenant devem gerar auditoria com ator, Tenant, ação, resultado, data/hora e metadados mínimos. | Definida | Criação, ativação, suspensão, encerramento, configuração, convite e alterações de Membership/roles são auditáveis. |
| BR-TEN-025 | Jobs, arquivos, cache, relatórios, exportações e integrações sobre dados tenant-owned devem carregar e validar Tenant Context durante toda execução. | Definida | Job ou exportação do A não processa, armazena ou entrega dados do B; ausência ou divergência de contexto é negada e registrada. |

### 2.2 Transições de Tenant

| Estado de origem | Transições permitidas | Observação |
|---|---|---|
| `PENDING` | `ACTIVE`, `CLOSED` | Ativação conclui cadastro/aprovação. |
| `ACTIVE` | `SUSPENDED`, `CLOSED` | Suspensão preserva dados; encerramento interrompe operação normal. |
| `SUSPENDED` | `ACTIVE`, `CLOSED` | Reativação requer autorização e política aprovada. |
| `CLOSED` | nenhuma | Reabertura exige fluxo e decisão futura; não é automática. |

### 2.3 Casos de teste mínimos

- Criar Tenant resulta em administrador inicial ativo.
- Tenant ativo não pode ficar sem administrador ativo.
- User sem Membership ativo não troca nem opera no Tenant.
- Trocar Tenant recalcula permissões e não reutiliza dados do contexto anterior.
- Tenant suspenso ou fechado bloqueia operações tenant-owned.
- Convite pendente não concede acesso operacional.
- Configurações, cache, arquivos, jobs e relatórios não cruzam Tenants.
- Alterações administrativas geram auditoria sem segredos.
- Privilégio de plataforma não concede acesso transversal sem autorização explícita.

## 3. Pacientes

Paciente representa a pessoa atendida ou administrada pela organização. O cadastro pertence ao Tenant atual; a identidade do paciente não é compartilhada automaticamente entre organizações.

### 3.1 Regras

| ID | Regra | Classificação | Critérios verificáveis |
|---|---|---|---|
| BR-PAT-001 | Todo Patient pertence a exatamente um Tenant e só pode ser criado, consultado, alterado ou arquivado dentro de Tenant Context válido. | Definida | User do Tenant A não acessa Patient do B por ID, busca, paginação, exportação ou referência indireta. |
| BR-PAT-002 | Criar, consultar, atualizar e arquivar Patient exige permissão explícita no Tenant atual. | Definida | User autenticado sem permissão apropriada não lê nem altera dados de Patient. |
| BR-PAT-003 | O cadastro de Patient deve conter somente os dados obrigatórios definidos para o fluxo; campos obrigatórios e regras de formato são validados no backend. | Definida | Cadastro sem campo obrigatório ou com formato inválido é recusado sem persistência parcial. |
| BR-PAT-004 | O conjunto definitivo de campos obrigatórios, documentos aceitos e validações específicas deve ser definido antes da implementação de produção. | Decisão pendente | A decisão documenta quais dados são obrigatórios, opcionais, sensíveis, normalizados e quais regras variam por tipo de atendimento. |
| BR-PAT-005 | Patient possui os estados `ACTIVE` e `ARCHIVED`. | Definida | Não é permitido persistir outro estado; mudança de estado é validada no backend. |
| BR-PAT-006 | Patient `ACTIVE` pode ser usado nos fluxos operacionais permitidos, incluindo agendamento quando o domínio Agenda assim exigir. | Definida | Criar operação que exija Patient ativo falha quando o Patient está arquivado. |
| BR-PAT-007 | Arquivar Patient impede novos usos operacionais, mas preserva seu histórico, vínculos e rastreabilidade. | Definida | Patient arquivado não aparece em listagens operacionais padrão nem recebe novo agendamento; consultas históricas autorizadas permanecem possíveis. |
| BR-PAT-008 | Reativar Patient arquivado exige autorização equivalente à de atualização e deve ser auditado. | Definida | User sem capacidade de alteração não reativa; reativação preserva o mesmo Tenant e histórico. |
| BR-PAT-009 | O MVP não utiliza exclusão física de Patient como fluxo normal. | Fora do MVP | Exclusão em endpoint ou interface não remove Patient nem seu histórico; descontinuação ocorre por arquivamento. |
| BR-PAT-010 | O sistema deve identificar possíveis duplicidades antes da criação ou alteração relevante de Patient. | Definida | Quando os critérios configurados indicarem possível duplicidade, o sistema apresenta ou retorna alerta e exige decisão explícita do usuário autorizado antes de criar novo registro. |
| BR-PAT-011 | Possível duplicidade não bloqueia automaticamente o cadastro enquanto não houver política aprovada de bloqueio. | Definida | O alerta não apaga nem mescla registros automaticamente; a ação tomada fica rastreável quando aplicável. |
| BR-PAT-012 | Os critérios, a normalização e a prioridade de comparação para duplicidade — por exemplo documento, nome, data de nascimento, telefone ou e-mail — devem ser definidos antes da produção. | Decisão pendente | A política aprovada declara campos, tratamento de ausência, correspondência aproximada e casos que bloqueiam ou apenas alertam. |
| BR-PAT-013 | Mesclagem de cadastros duplicados exige processo explícito, reversibilidade ou trilha de investigação adequada e preservação de referências históricas. | Futuro | Nenhum fluxo do MVP mescla automaticamente Patients ou redireciona silenciosamente histórico e agendamentos. |
| BR-PAT-014 | Atualizações devem preservar consistência do cadastro e não podem mover Patient para outro Tenant. | Definida | Qualquer tentativa de alterar `tenant_id` de Patient é negada; alterações inválidas não substituem valores anteriores. |
| BR-PAT-015 | Dados de Patient devem ser minimizados conforme a finalidade do produto e não podem ser expostos em listas, logs, erros ou auditoria além do necessário. | Definida | Listagens retornam apenas campos necessários; logs e mensagens de erro não incluem dados sensíveis desnecessários. |
| BR-PAT-016 | Dados clínicos detalhados, prontuário, consentimentos, responsáveis, contatos de emergência e regras de dados de menores exigem especificação própria antes de implementação. | Fora do MVP | O MVP não presume que esses dados integram o cadastro básico de Patient. |
| BR-PAT-017 | Pesquisas e listagens de Patients devem aplicar Tenant Context e autorização antes de filtros, ordenação e paginação. | Definida | Filtro ou paginação não revela quantidade, existência ou dados de Patients de outro Tenant. |
| BR-PAT-018 | Uma referência de Patient usada por outro domínio deve ser validada no backend quanto ao Tenant, estado e permissão antes da operação. | Definida | Agendamento ou outro comando não vincula recurso do Tenant A a Patient do Tenant B nem usa Patient arquivado quando a regra exigir ativo. |
| BR-PAT-019 | Criação, atualização, arquivamento, reativação e decisão relevante sobre possível duplicidade devem gerar auditoria com ator, Tenant, Patient, ação, resultado e data/hora. | Definida | Auditoria permite identificar quem executou a ação sem armazenar o conteúdo completo de dados sensíveis. |
| BR-PAT-020 | Acesso a dados de Patient por administrador de plataforma ou suporte não é implícito e exige capacidade e escopo explicitamente definidos. | Definida | Role de plataforma sem autorização transversal documentada não consulta registros de Patient. |

### 3.2 Transições de Patient

| Estado de origem | Transições permitidas | Observação |
|---|---|---|
| `ACTIVE` | `ARCHIVED` | Arquivamento retira o Patient do uso operacional padrão e preserva histórico. |
| `ARCHIVED` | `ACTIVE` | Reativação exige autorização e auditoria. |

### 3.3 Casos de teste mínimos

- User do Tenant A não lê, altera, arquiva nem agenda Patient do Tenant B.
- Cadastro inválido não cria registro parcial.
- Patient arquivado não é elegível para novos fluxos operacionais.
- Reativação retorna Patient ao uso permitido sem alterar Tenant ou histórico.
- Busca, paginação e filtros não vazam existência ou dados entre Tenants.
- Possível duplicidade gera alerta sem mesclagem ou exclusão automática.
- Tentativa de trocar `tenant_id` do Patient é negada.
- Auditoria registra alterações relevantes sem expor dados sensíveis desnecessários.

## 4. Agenda

Agenda organiza compromissos operacionais do Tenant. Um agendamento reserva um intervalo para um Patient e, quando aplicável, para um ou mais profissionais ou recursos do mesmo Tenant.

### 4.1 Regras

| ID | Regra | Classificação | Critérios verificáveis |
|---|---|---|---|
| BR-AGE-001 | Todo Appointment pertence a exatamente um Tenant e só pode ser criado, consultado ou alterado em Tenant Context válido. | Definida | User do Tenant A não acessa nem modifica agendamento do Tenant B por ID, busca, calendário, exportação ou referência indireta. |
| BR-AGE-002 | Criar, consultar, alterar, confirmar, cancelar, concluir ou registrar ausência exige permissão explícita no Tenant atual. | Definida | User sem permissão apropriada não executa a ação, mesmo sendo autor ou profissional relacionado ao Appointment. |
| BR-AGE-003 | Todo Appointment deve possuir Patient, início, fim e estado válidos; início deve ser estritamente anterior ao fim. | Definida | Criação ou alteração com Patient ausente, intervalo vazio, negativo ou inválido é negada sem persistência parcial. |
| BR-AGE-004 | Patient vinculado ao Appointment deve pertencer ao Tenant atual e estar `ACTIVE`. | Definida | Não é possível agendar Patient de outro Tenant ou Patient arquivado. |
| BR-AGE-005 | Profissional ou recurso vinculado ao Appointment, quando aplicável, deve pertencer ao Tenant atual e estar disponível para uso operacional. | Definida | Não é possível associar recurso de outro Tenant, inativo ou indisponível ao agendamento. |
| BR-AGE-006 | O modelo mínimo de recurso para o MVP deve definir se cada Appointment exige profissional, sala, equipamento ou outro recurso, bem como as regras de capacidade. | Decisão pendente | A decisão declara recursos obrigatórios, capacidade por recurso e quais combinações podem atender ao mesmo Appointment. |
| BR-AGE-007 | O intervalo de um Appointment é tratado como `[start_at, end_at)`: o fim não ocupa o mesmo instante do início de outro agendamento. | Definida | Dois agendamentos consecutivos, com fim do primeiro igual ao início do segundo, não conflitam apenas por esse limite compartilhado. |
| BR-AGE-008 | Um recurso com capacidade unitária não pode possuir dois Appointments ativos com intervalos sobrepostos. | Definida | O sistema recusa criação ou alteração que sobreponha qualquer parte do intervalo de Appointment `SCHEDULED` ou `CONFIRMED` do mesmo recurso. |
| BR-AGE-009 | A verificação de conflito deve ocorrer no backend no momento de persistir criação ou alteração, com proteção contra concorrência. | Definida | Duas tentativas concorrentes para o mesmo recurso e horário não resultam em dupla reserva. |
| BR-AGE-010 | O cálculo de disponibilidade deve considerar Tenant, recurso, intervalo, estado do Appointment e bloqueios operacionais aprovados. | Definida | Consulta de disponibilidade não oferece horário já reservado ou pertencente a outro Tenant. |
| BR-AGE-011 | Horários de trabalho, folgas, feriados, bloqueios de agenda, fusos horários, duração padrão e antecedência mínima exigem política específica antes da produção. | Decisão pendente | A política define origem de horário, timezone do Tenant, exceções e comportamento em horário inválido. |
| BR-AGE-012 | Appointment possui um dos estados `SCHEDULED`, `CONFIRMED`, `CANCELLED`, `COMPLETED` ou `NO_SHOW`. | Definida | Não é permitido persistir estado fora do catálogo; toda transição é validada no backend. |
| BR-AGE-013 | Criar Appointment produz estado inicial `SCHEDULED`, salvo fluxo futuro explicitamente aprovado. | Definida | Novo Appointment válido é criado como `SCHEDULED` e passa a participar da verificação de conflitos. |
| BR-AGE-014 | `SCHEDULED` pode transitar para `CONFIRMED`, `CANCELLED`, `COMPLETED` ou `NO_SHOW`; `CONFIRMED` pode transitar para `CANCELLED`, `COMPLETED` ou `NO_SHOW`. | Definida | Transições fora da tabela são negadas; transições terminais não são reabertas silenciosamente. |
| BR-AGE-015 | `CANCELLED`, `COMPLETED` e `NO_SHOW` são estados terminais no MVP. | Definida | Não é permitido confirmar, concluir ou alterar diretamente um Appointment terminal; novo atendimento exige novo Appointment. |
| BR-AGE-016 | Alterar horário, Patient ou recurso de Appointment ativo deve executar novamente todas as validações de escopo, estado e conflito antes da persistência. | Definida | Alteração que cria conflito ou aponta para Patient/recurso inválido é negada e mantém dados anteriores. |
| BR-AGE-017 | A regra de alteração ou cancelamento próximo do horário, motivo obrigatório e responsáveis por confirmar/concluir/registrar ausência deve ser definida antes da produção. | Decisão pendente | A política aprovada declara janelas, exceções, motivo, permissões e impacto operacional. |
| BR-AGE-018 | Cancelamento libera a reserva de recursos; concluído e ausência preservam o histórico e não são considerados disponibilidade futura. | Definida | Após cancelamento, o mesmo intervalo pode ser reservado se não houver outro bloqueio; Appointment terminal continua consultável por usuários autorizados. |
| BR-AGE-019 | Recorrência, lista de espera, overbooking, encaixe, múltiplos atendimentos simultâneos e notificações automáticas são capacidades futuras. | Futuro | MVP não cria séries recorrentes, não excede capacidade definida e não envia notificações como condição do agendamento. |
| BR-AGE-020 | Criação, alteração, confirmação, cancelamento, conclusão, ausência e tentativa de conflito devem gerar auditoria com ator, Tenant, Appointment, ação, resultado e data/hora. | Definida | Auditoria permite reconstruir o ciclo do Appointment sem armazenar dados clínicos ou segredos desnecessários. |
| BR-AGE-021 | Listagens, calendários e relatórios de agenda devem aplicar Tenant Context e autorização antes de filtros, intervalo, paginação e agregação. | Definida | Intervalo de datas ou filtro de recurso não revela quantidade, detalhes ou disponibilidade de outro Tenant. |
| BR-AGE-022 | Dados clínicos, procedimentos, faturamento, prescrição e prontuário não fazem parte do Appointment básico do MVP e exigem domínios e regras próprios. | Fora do MVP | O fluxo de Agenda não presume persistência nem exposição desses dados. |

### 4.2 Transições de Appointment

| Estado de origem | Transições permitidas | Observação |
|---|---|---|
| `SCHEDULED` | `CONFIRMED`, `CANCELLED`, `COMPLETED`, `NO_SHOW` | Reserva recursos enquanto ativo. |
| `CONFIRMED` | `CANCELLED`, `COMPLETED`, `NO_SHOW` | Reserva recursos enquanto ativo. |
| `CANCELLED` | nenhuma | Libera reserva; preserva histórico. |
| `COMPLETED` | nenhuma | Preserva histórico do atendimento agendado. |
| `NO_SHOW` | nenhuma | Preserva ausência e histórico. |

### 4.3 Casos de teste mínimos

- User do Tenant A não consulta nem altera Appointment do Tenant B.
- Patient arquivado ou de outro Tenant não pode ser agendado.
- Intervalo inválido é recusado.
- Sobreposição em recurso unitário é recusada, inclusive em requisições concorrentes.
- Agendamentos consecutivos não conflitam.
- Cancelamento libera disponibilidade; estados terminais não são reabertos.
- Alterar horário ou recurso reaplica validação de conflito.
- Calendário, filtros e paginação não vazam dados entre Tenants.
- Alterações e conflitos relevantes geram auditoria sem dados sensíveis desnecessários.

## 5. Arquivos & Anexos

File representa os metadados de um objeto armazenado externamente e associado a um recurso permitido. O arquivo físico não substitui as regras de Tenant, autorização ou vínculo de domínio.

### 5.1 Regras

| ID | Regra | Classificação | Critérios verificáveis |
|---|---|---|---|
| BR-FIL-001 | Todo File pertence a exatamente um Tenant e só pode ser criado, consultado, baixado ou removido dentro de Tenant Context válido. | Definida | User do Tenant A não acessa File do B por ID, URL, chave de armazenamento ou referência de recurso. |
| BR-FIL-002 | Upload, consulta, download e remoção exigem permissão explícita para o recurso proprietário e para a ação solicitada. | Definida | Conhecer a chave, nome ou URL de um objeto não concede leitura, gravação nem exclusão. |
| BR-FIL-003 | Todo File deve registrar, no mínimo, Tenant, recurso proprietário, nome original, nome/chave interna, tipo de conteúdo, tamanho, autor e datas relevantes. | Definida | Não é possível concluir upload sem metadados mínimos e vínculo válido com recurso do mesmo Tenant. |
| BR-FIL-004 | O recurso proprietário deve existir, pertencer ao Tenant atual e aceitar anexos segundo regra do domínio correspondente. | Definida | Não se associa File a Patient, Appointment ou recurso inexistente, de outro Tenant ou que não suporte anexos. |
| BR-FIL-005 | Chaves de armazenamento devem ser geradas pelo servidor e possuir namespace por Tenant; nome informado pelo usuário não é usado como chave confiável. | Definida | Dois Tenants não recebem o mesmo caminho lógico; alterar nome original não permite sobrescrever objeto de outro Tenant. |
| BR-FIL-006 | Tipo, tamanho máximo, quantidade por recurso e tipos de arquivo aceitos devem ser validados no backend antes de disponibilizar o objeto. | Definida | Upload fora de limite ou tipo não permitido é negado e não fica disponível para download. |
| BR-FIL-007 | O catálogo de tipos permitidos, limites por Tenant/recurso e método de inspeção de conteúdo devem ser definidos antes da produção. | Decisão pendente | A política aprovada define MIME, extensão, tamanho, quota, tratamento de divergência e resposta ao usuário. |
| BR-FIL-008 | O tipo de conteúdo declarado pelo cliente não é prova suficiente do conteúdo do arquivo. | Definida | A validação não depende apenas do cabeçalho ou extensão enviada; divergências seguem a política de segurança. |
| BR-FIL-009 | Arquivos enviados não ficam publicamente acessíveis por padrão. | Definida | Não existe URL pública permanente que permita download sem autenticação e autorização válidas. |
| BR-FIL-010 | O download deve validar novamente User, Tenant Context, Membership, permissão e vínculo do File com o recurso proprietário. | Definida | Um link obtido por usuário autorizado não permite acesso posterior por usuário sem autorização ou de outro Tenant. |
| BR-FIL-011 | URLs assinadas, quando usadas, devem ter escopo mínimo, expiração limitada e só ser emitidas após autorização. | Definida | URL expirada, alterada ou emitida para recurso não autorizado não concede acesso. |
| BR-FIL-012 | Remover File no MVP é exclusão lógica: o arquivo deixa de estar disponível operacionalmente, mantendo metadados e auditoria conforme política de retenção. | Definida | File removido não aparece nem é baixado em fluxos normais; evento e vínculo histórico permanecem rastreáveis. |
| BR-FIL-013 | Exclusão física do objeto, retenção, restauração e limpeza de órfãos exigem política de segurança, privacidade e operação antes de produção. | Decisão pendente | A política define prazo, responsáveis, falhas de limpeza, recuperação e tratamento de objeto sem metadado. |
| BR-FIL-014 | Malware scanning, quarentena, OCR, versionamento e pré-visualização são capacidades futuras, salvo obrigação de segurança definida antes da produção. | Futuro | MVP não promete visualização, extração de texto ou histórico de versões; arquivos suspeitos seguem política aprovada. |
| BR-FIL-015 | Arquivos não devem armazenar segredos em metadados, logs, URLs ou eventos de auditoria. | Definida | Logs e auditoria não expõem conteúdo, token de URL assinada ou dado sensível desnecessário. |
| BR-FIL-016 | Upload interrompido ou falho não pode produzir File disponível sem objeto válido, nem objeto definitivo sem tratamento de órfão. | Definida | Falha em qualquer etapa deixa o File indisponível e gera registro técnico suficiente para reconciliação. |
| BR-FIL-017 | Jobs, cache, exportações e integrações que manipularem arquivos devem carregar e validar Tenant Context durante toda a execução. | Definida | Processamento do Tenant A não lê, transforma ou entrega objeto do Tenant B. |
| BR-FIL-018 | Criação, disponibilização, download, remoção e falha relevante de arquivo devem gerar auditoria com ator, Tenant, File, recurso proprietário, ação, resultado e data/hora. | Definida | Auditoria permite investigação sem registrar conteúdo do arquivo ou dados sensíveis desnecessários. |

### 5.2 Casos de teste mínimos

- User do Tenant A não obtém File do Tenant B por ID, URL ou chave.
- Upload inválido não deixa objeto disponível nem metadado incompleto.
- File só é associado a recurso existente, autorizado e do mesmo Tenant.
- Nome ou extensão manipulados não permitem sobrescrita nem ignoram validação.
- Download exige autorização atual; URL assinada expira.
- Remoção lógica bloqueia download e preserva auditoria.
- Falhas deixam artefatos reconciliáveis, sem acesso indevido.
- Logs e auditoria não expõem conteúdo ou tokens de acesso.

## 6. Relatórios & Exportações

Relatórios consolidam informações autorizadas do Tenant. Exportações são artefatos derivados de uma solicitação autorizada, não um meio de contornar filtros, permissões ou isolamento.

### 6.1 Regras

| ID | Regra | Classificação | Critérios verificáveis |
|---|---|---|---|
| BR-REP-001 | Todo relatório, consulta agregada e exportação pertence a um Tenant e executa somente no Tenant Context validado. | Definida | Solicitação no Tenant A não consulta, agrega nem entrega dados do Tenant B. |
| BR-REP-002 | Solicitar, visualizar, baixar ou administrar relatório/exportação exige permissão explícita para o tipo de dado e ação no Tenant atual. | Definida | User sem permissão não vê catálogo, resultado, estado ou arquivo de exportação não autorizado. |
| BR-REP-003 | Filtros, ordenação, agrupamento, intervalo e paginação são validados no backend e aplicados após Tenant Context e autorização. | Definida | Parâmetro manipulado não amplia escopo, não remove filtro obrigatório e não revela contagens entre Tenants. |
| BR-REP-004 | Um relatório só pode expor campos compatíveis com a permissão e finalidade do solicitante. | Definida | Relatório de acesso limitado não inclui campos sensíveis, detalhes de Patient ou dados administrativos além do escopo aprovado. |
| BR-REP-005 | O catálogo de relatórios do MVP, suas fontes, filtros obrigatórios, campos exibidos e permissões deve ser definido antes da implementação. | Decisão pendente | Cada relatório aprovado possui finalidade, dados de origem, regras de cálculo, escopo, formato e permission requerida documentados. |
| BR-REP-006 | Resultado de relatório deve indicar filtros, período, Tenant e instante de geração quando esses metadados forem necessários para interpretação. | Definida | Usuário autorizado consegue distinguir resultado gerado para período ou filtro diferente, sem expor metadados de outro Tenant. |
| BR-REP-007 | Solicitação de exportação cria um processo rastreável com estados `PENDING`, `RUNNING`, `COMPLETED`, `FAILED` ou `EXPIRED`. | Definida | Estado fora do catálogo é recusado; resultado só fica disponível em `COMPLETED`. |
| BR-REP-008 | Geração assíncrona preserva Tenant, solicitante, filtros autorizados e contexto necessário do início ao fim do job. | Definida | Worker não depende de contexto HTTP; job do Tenant A não processa dados do B. |
| BR-REP-009 | A permissão e o estado atual do solicitante e Tenant devem ser revalidados antes da entrega do resultado. | Definida | Suspensão de Membership/Tenant ou remoção de permissão impede download de exportação concluída, conforme autorização atual. |
| BR-REP-010 | Arquivo de exportação segue as regras de Arquivos & Anexos: armazenamento isolado, acesso não público, vínculo, expiração e auditoria. | Definida | Conhecer chave ou URL não permite baixar exportação sem autorização atual. |
| BR-REP-011 | Formatos permitidos, limites de tamanho, intervalo máximo, número de linhas, quantidade de jobs por usuário/Tenant e tempo de expiração devem ser definidos antes da produção. | Decisão pendente | A política descreve limites, fila, rejeição, expiração e resposta em caso de excesso. |
| BR-REP-012 | Exportação não deve incluir dados ou colunas que não estariam disponíveis para visualização autorizada no mesmo escopo. | Definida | Não é possível usar exportação para obter campos ocultos, mais registros ou dados de outro Tenant. |
| BR-REP-013 | Resultados em cache devem ser namespaceados por Tenant, relatório, filtros, permissão/escopo aplicável e versão de cálculo quando necessário. | Definida | Cache hit de relatório não entrega ao Tenant A resultado gerado para B ou para escopo mais amplo. |
| BR-REP-014 | Cancelamento de job é permitido somente enquanto não terminal e deve impedir entrega de resultado parcial ou não autorizado. | Definida | Job cancelado não produz arquivo disponível; artefatos parciais são tratados segundo política operacional. |
| BR-REP-015 | Reagendamento automático, relatórios recorrentes, dashboards em tempo real, compartilhamento externo e distribuição por e-mail são capacidades futuras. | Futuro | MVP não envia exportações a destinatários externos nem cria execução recorrente sem solicitação autorizada. |
| BR-REP-016 | BI avançado, indicadores financeiros completos, consolidação entre Tenants e análises clínicas dependem de domínios e políticas próprios. | Fora do MVP | MVP não agrega dados de múltiplas organizações nem presume acesso clínico/financeiro ampliado. |
| BR-REP-017 | Solicitação, início, conclusão, falha, cancelamento, expiração e download de exportação devem gerar auditoria com ator, Tenant, tipo, filtros mínimos, resultado e data/hora. | Definida | Auditoria permite investigar geração e entrega sem registrar conteúdo integral ou dados sensíveis desnecessários. |
| BR-REP-018 | Falhas de geração não devem expor query, stack trace, dados de outro Tenant ou detalhes internos ao solicitante. | Definida | Resposta pública informa estado ou erro seguro; detalhes técnicos permanecem em observabilidade restrita. |

### 6.2 Transições de exportação

| Estado de origem | Transições permitidas | Observação |
|---|---|---|
| `PENDING` | `RUNNING`, `FAILED` | Aguardando processamento. |
| `RUNNING` | `COMPLETED`, `FAILED` | Só resultado completo pode ser entregue. |
| `COMPLETED` | `EXPIRED` | Resultado disponível até expiração definida. |
| `FAILED` | nenhuma | Nova tentativa exige nova solicitação ou política futura explícita. |
| `EXPIRED` | nenhuma | Resultado deixa de estar disponível. |

### 6.3 Casos de teste mínimos

- Relatório e exportação do Tenant A não retornam dados do B.
- Filtros manipulados não ampliam escopo nem revelam contagens externas.
- Exportação respeita os mesmos campos e permissions da visualização.
- Job assíncrono preserva Tenant, solicitante e filtros autorizados.
- Suspensão de Tenant/Membership ou remoção de permission bloqueia entrega posterior.
- Cache não cruza Tenant, filtro ou escopo.
- Resultado parcial, falho, cancelado ou expirado não é baixado.
- Auditoria registra ciclo da exportação sem conteúdo sensível.

## 7. Auditoria & Rastreabilidade

Auditoria registra eventos relevantes de negócio, segurança e administração para investigação. Ela não substitui logs técnicos nem deve se transformar em cópia indiscriminada de dados sensíveis.

### 7.1 Regras

| ID | Regra | Classificação | Critérios verificáveis |
|---|---|---|---|
| BR-AUD-001 | Todo AuditEvent deve conter identificador, data/hora, ação, resultado, tipo de recurso e contexto de Tenant quando a operação for tenant-owned. | Definida | Evento sem campos mínimos obrigatórios não é persistido como auditoria válida. |
| BR-AUD-002 | O evento deve registrar ator quando identificado; para operações anônimas ou falhas de autenticação, deve registrar contexto técnico mínimo sem inventar identidade. | Definida | Login falho pode ser investigado sem atribuir ação a User inexistente. |
| BR-AUD-003 | Eventos de auditoria devem ser gerados para operações definidas pelos domínios, incluindo identidade, administração de Tenant, Memberships, Patients, Agenda, Files e Exportações. | Definida | Executar ação auditável gera evento com ação e resultado coerentes; falha relevante também é registrável conforme política. |
| BR-AUD-004 | O evento de auditoria deve permitir investigar quem fez, o que fez, quando ocorreu, em qual Tenant e sobre qual recurso, sem exigir acesso a logs técnicos. | Definida | Consulta autorizada permite correlacionar ator, ação, recurso, resultado e momento do evento. |
| BR-AUD-005 | Metadados devem ser mínimos, estruturados e adequados à finalidade de investigação. | Definida | Não são armazenados senha, token completo, segredo, conteúdo de arquivo ou dados sensíveis não necessários. |
| BR-AUD-006 | Auditoria deve registrar a versão ou identificador de correlação da operação quando necessário para ligar eventos de um mesmo fluxo. | Definida | Job, exportação ou operação distribuída pode ser investigado por correlação sem misturar Tenants. |
| BR-AUD-007 | Alterações de recurso devem registrar o resultado e, quando necessário, resumo seguro de campos afetados, mas não uma cópia integral de dados pessoais ou clínicos. | Definida | Alteração de Patient é rastreável sem expor cadastro completo no evento. |
| BR-AUD-008 | AuditEvent é imutável para usuários e fluxos comuns de negócio. | Definida | Não existe operação normal que edite ou apague seletivamente conteúdo de auditoria já persistido. |
| BR-AUD-009 | Correção de informação operacional não altera eventos históricos; gera nova ação ou evento de correção rastreável. | Definida | A auditoria preserva sequência de fatos sem reescrever evento anterior. |
| BR-AUD-010 | O acesso à consulta de auditoria exige permissão explícita e respeita Tenant Context, escopo do solicitante e sensibilidade do evento. | Definida | User sem permissão não lista eventos; User do A não consulta eventos do B. |
| BR-AUD-011 | Acesso administrativo transversal à auditoria exige capacidade de plataforma, finalidade e escopo explicitamente aprovados. | Definida | Ser administrador de Tenant não autoriza consultar auditoria de outro Tenant; suporte não tem acesso implícito. |
| BR-AUD-012 | Filtros, busca, ordenação e paginação de auditoria são aplicados depois da autorização e nunca ampliam o escopo do Tenant. | Definida | Buscar por ID, User ou período não revela existência de eventos de outro Tenant. |
| BR-AUD-013 | Logs técnicos e eventos de auditoria são artefatos distintos: logs servem à operação técnica; auditoria serve à rastreabilidade de negócio e segurança. | Definida | Ausência de log técnico não elimina evento de auditoria obrigatório, e consulta de auditoria não expõe stack trace. |
| BR-AUD-014 | Falha para gravar auditoria de operação crítica deve seguir política explícita de consistência antes da produção. | Decisão pendente | A política define quais ações falham integralmente, quais admitem retentativa e como alertas são acionados. |
| BR-AUD-015 | Retenção, arquivamento, imutabilidade reforçada, exportação e descarte de eventos devem ser definidos com requisitos de segurança, privacidade e obrigações legais. | Decisão pendente | A política define prazos, acesso, restauração, descarte e tratamento de solicitações legais. |
| BR-AUD-016 | Consulta e exportação de auditoria devem observar as mesmas regras de autorização, Tenant e minimização aplicáveis a Relatórios & Exportações. | Definida | Exportar eventos não inclui dados, Tenants ou colunas fora do escopo autorizado. |
| BR-AUD-017 | Monitoramento de padrões suspeitos, alertas de segurança, trilhas invioláveis e integração com SIEM são capacidades futuras. | Futuro | MVP registra eventos essenciais, mas não promete detecção avançada ou integração externa. |
| BR-AUD-018 | Alteração ou exclusão física de eventos de auditoria por interface comum está fora do MVP. | Fora do MVP | MVP não oferece tela ou API para editar, ocultar ou excluir eventos individualmente. |

### 7.2 Casos de teste mínimos

- Ações auditáveis geram evento com ator/contexto, Tenant, recurso, resultado e data/hora.
- Evento não registra senha, token, conteúdo de arquivo ou dado sensível desnecessário.
- Usuário não autorizado não consulta auditoria; Tenant A não consulta B.
- Filtros e paginação não revelam eventos fora de escopo.
- Alteração posterior de recurso não reescreve evento antigo.
- Falha técnica não expõe detalhes internos na consulta de auditoria.
- Exportação de auditoria respeita as mesmas permissões e isolamento da consulta.

## 8. Profissionais & Recursos

Profissional ou Resource representa pessoa, sala, equipamento ou capacidade operacional necessária para a Agenda. Sua existência não implica autorização de acesso nem disponibilidade para reserva.

### 8.1 Regras

| ID | Regra | Classificação | Critérios verificáveis |
|---|---|---|---|
| BR-RES-001 | Todo profissional ou recurso pertence a exatamente um Tenant e só pode ser gerenciado no Tenant Context válido. | Definida | User do Tenant A não cria, consulta, altera ou desativa recurso do B por ID, busca ou vínculo de agenda. |
| BR-RES-002 | Criar, consultar, atualizar e desativar profissional/recurso exige permissão explícita no Tenant atual. | Definida | User sem capacidade correspondente não altera catálogo ou disponibilidade operacional. |
| BR-RES-003 | O recurso deve possuir tipo, nome de exibição, estado e capacidade válidos; demais atributos dependem de seu tipo e da política aprovada. | Definida | Cadastro sem campos mínimos ou com capacidade inválida é recusado sem persistência parcial. |
| BR-RES-004 | O catálogo de tipos do MVP deve distinguir, no mínimo, profissional, sala e equipamento quando esses forem necessários à operação, sem confundir Resource com User ou Membership. | Decisão pendente | A decisão define tipos habilitados, atributos obrigatórios e quais tipos podem ser agendados. |
| BR-RES-005 | Profissional/recurso possui estado `ACTIVE` ou `INACTIVE`. | Definida | Não é permitido persistir estado fora do catálogo; só `ACTIVE` pode receber novas reservas. |
| BR-RES-006 | Desativar recurso impede novos Appointments, mas preserva sua relação com agendamentos e histórico existentes. | Definida | Recurso inativo não aparece em disponibilidade para novas reservas; Appointments passados continuam consultáveis. |
| BR-RES-007 | Não é permitido desativar recurso quando houver Appointment futuro ativo vinculado sem que exista resolução explícita para esses agendamentos. | Definida | A operação é negada ou exige remanejamento/cancelamento autorizado antes da desativação. |
| BR-RES-008 | Reativar recurso exige autorização administrativa/operacional e não altera retroativamente Appointments passados. | Definida | Resource reativado só se torna elegível para reservas futuras após mudança de estado auditada. |
| BR-RES-009 | Capacidade do recurso deve ser positiva e é considerada no cálculo de disponibilidade e conflito da Agenda. | Definida | Recurso de capacidade unitária não aceita sobreposição; regra para capacidade maior segue política aprovada. |
| BR-RES-010 | Agendamento com capacidade superior a um, múltiplos recursos obrigatórios e reserva de equipe exigem modelo de capacidade e alocação definido antes da produção. | Decisão pendente | A política especifica consumo de capacidade, conflito, alteração e cancelamento. |
| BR-RES-011 | Disponibilidade de recurso considera estado, Tenant, horário de trabalho e bloqueios aplicáveis; não é inferida somente pela ausência de Appointment. | Definida | Recurso fora de horário ou bloqueado não é oferecido como disponível, mesmo sem reserva conflitante. |
| BR-RES-012 | Horários de trabalho, folgas, férias, manutenção, bloqueios, fuso horário e regras de exceção devem ser definidos antes da produção. | Decisão pendente | A política declara origem das agendas, recorrência, prioridade de bloqueios e comportamento em exceções. |
| BR-RES-013 | Vínculo entre profissional e User é opcional e não é automático: User concede acesso ao sistema; profissional representa capacidade operacional. | Definida | Criar ou desativar User não cria, remove ou altera profissional automaticamente sem fluxo explícito. |
| BR-RES-014 | Credenciais profissionais, especialidades, registros de conselho, unidades e permissões clínicas exigem especificação própria. | Futuro | MVP não valida conselho profissional, especialidade ou escopo clínico como condição genérica de agenda. |
| BR-RES-015 | Criação, alteração, ativação, desativação, bloqueio e mudança relevante de capacidade/disponibilidade devem gerar auditoria. | Definida | Evento registra ator, Tenant, Resource, ação, resultado e data/hora sem dados sensíveis desnecessários. |
| BR-RES-016 | Exclusão física de profissional/recurso com histórico de Appointment está fora do MVP. | Fora do MVP | Descontinuação ocorre por desativação; referências históricas permanecem preservadas. |

### 8.2 Transições de profissional/recurso

| Estado de origem | Transições permitidas | Observação |
|---|---|---|
| `ACTIVE` | `INACTIVE` | Requer resolução de Appointments futuros ativos vinculados. |
| `INACTIVE` | `ACTIVE` | Reativação devolve elegibilidade para reservas futuras. |

### 8.3 Casos de teste mínimos

- Recurso de um Tenant não é associado a Appointment de outro.
- Recurso inativo, bloqueado ou fora de horário não aparece como disponível.
- Desativação com Appointment futuro ativo exige resolução explícita.
- Capacidade unitária impede sobreposição pela Agenda.
- User e profissional não são criados ou removidos automaticamente um pelo outro.
- Alterações de estado, capacidade e disponibilidade geram auditoria.
- Histórico de Appointment preserva referência a recurso desativado.

## 9. Financeiro

O Financeiro é um domínio futuro. Estas regras preservam a segurança, o isolamento e a rastreabilidade necessários para sua evolução, mas não autorizam implementação de faturamento ou contabilidade completos no MVP.

### 9.1 Regras

| ID | Regra | Classificação | Critérios verificáveis |
|---|---|---|---|
| BR-FIN-001 | Todo lançamento financeiro pertence a exatamente um Tenant e só pode ser criado, consultado ou alterado em Tenant Context válido. | Definida | User do Tenant A não acessa lançamento do B por ID, filtro, relatório ou exportação. |
| BR-FIN-002 | Criar, consultar, aprovar, cancelar ou estornar lançamento exige permissão financeira explícita no Tenant atual. | Definida | User sem permission financeira não consulta valores nem altera lançamentos. |
| BR-FIN-003 | Lançamento financeiro deve possuir valor, moeda, natureza, data relevante, estado, origem e referência de Tenant válidos. | Futuro | Implementação futura rejeita valores inválidos, ausência de origem e alterações de Tenant. |
| BR-FIN-004 | O catálogo de naturezas, contas, centros de custo, categorias, formas de pagamento e regras de competência deve ser definido antes de qualquer implementação. | Decisão pendente | Política aprovada define classificação, validações e relações entre esses conceitos. |
| BR-FIN-005 | Estados de lançamento, transições, aprovação, liquidação, cancelamento, estorno e conciliação devem ser explicitamente definidos antes da produção. | Decisão pendente | Nenhum valor livre de estado ou transição implícita é usado em implementação futura. |
| BR-FIN-006 | Lançamento confirmado não deve ser alterado de forma destrutiva; correção deve ocorrer por operação rastreável de ajuste, cancelamento ou estorno conforme política. | Futuro | Histórico permite distinguir fato original, correção e responsável, sem sobrescrita silenciosa. |
| BR-FIN-007 | Estorno deve preservar vínculo com o lançamento de origem, motivo, ator e data/hora. | Futuro | Não é possível estornar lançamento de outro Tenant ou produzir estorno sem referência válida. |
| BR-FIN-008 | Dados financeiros não podem ser expostos em relatórios, exportações, logs ou auditoria além do escopo autorizado. | Definida | Relatório sem permission financeira não revela valores, totais ou metadados sensíveis. |
| BR-FIN-009 | Referência opcional a Patient ou Appointment deve pertencer ao mesmo Tenant e não transforma o Financeiro em prontuário clínico. | Futuro | Lançamento não vincula recursos de Tenants diferentes e não armazena dados clínicos desnecessários. |
| BR-FIN-010 | Integrações bancárias, emissão fiscal, convênios, faturamento, cobrança recorrente, parcelamento e conciliação automática estão fora do MVP. | Fora do MVP | MVP não cria obrigações, documentos fiscais ou operações externas financeiras. |
| BR-FIN-011 | Moeda, arredondamento, impostos, juros, descontos, vencimento, inadimplência e regras de cálculo exigem validação de negócio e contábil antes da produção. | Decisão pendente | Cada cálculo futuro possui fonte, precisão, arredondamento e responsabilidade documentados. |
| BR-FIN-012 | Criação, aprovação, alteração, cancelamento, estorno e falha relevante de lançamento devem gerar auditoria completa. | Futuro | Auditoria registra ator, Tenant, lançamento, ação, resultado, motivo e data/hora sem expor dados excessivos. |
| BR-FIN-013 | Exclusão física de lançamento financeiro não é permitida como comportamento operacional comum. | Futuro | Correções preservam histórico por operações rastreáveis; descarte depende de política legal de retenção. |
| BR-FIN-014 | Implementação do Financeiro requer revisão de privacidade, segurança, requisitos contábeis, fiscais e jurídicos aplicáveis. | Decisão pendente | Antes de produção, decisões e responsabilidades são registradas e validadas com as partes competentes. |

### 9.2 Casos de teste mínimos para evolução futura

- Isolamento entre Tenants é aplicado a lançamentos, relatórios e exportações.
- Permission financeira é exigida para leitura e alteração.
- Correções e estornos preservam vínculo e trilha de auditoria.
- Dados clínicos não são duplicados em lançamentos.
- Cálculos e integrações só entram após políticas aprovadas.

## 10. Notificações

Notificações são comunicações operacionais futuras. Elas não substituem o estado oficial do domínio, a autorização no backend ou a consulta segura da aplicação.

### 10.1 Regras

| ID | Regra | Classificação | Critérios verificáveis |
|---|---|---|---|
| BR-NOT-001 | Toda notificação é associada a Tenant, evento de origem, destinatário, canal, estado e data/hora. | Futuro | Implementação futura não envia notificação sem contexto e origem rastreáveis. |
| BR-NOT-002 | A emissão de notificação deve respeitar Tenant Context e só usar destinatários autorizados ou dados de contato permitidos pela política aplicável. | Definida | Evento do Tenant A não gera comunicação para destinatário ou contato do Tenant B. |
| BR-NOT-003 | O domínio de origem continua sendo a fonte de verdade; falha, atraso ou duplicidade de notificação não altera estado de Appointment, Patient ou outro recurso. | Definida | Agendamento permanece válido conforme seu próprio estado mesmo quando entrega de lembrete falha. |
| BR-NOT-004 | O catálogo de eventos notificáveis, destinatários, canais, templates e prioridade deve ser definido antes de implementação. | Decisão pendente | Política aprovada define quais eventos podem notificar, quem recebe e em quais condições. |
| BR-NOT-005 | Preferências, consentimento, opt-in/opt-out, base legal e exceções para mensagens transacionais exigem validação de privacidade e negócio antes da produção. | Decisão pendente | Nenhum canal externo é ativado sem política documentada para coleta, mudança e prova de preferência. |
| BR-NOT-006 | Conteúdo deve obedecer minimização de dados: não incluir dado clínico, segredo, token ou informação sensível além do necessário ao propósito. | Definida | Template não expõe prontuário, senha, token completo ou dado de outro Tenant. |
| BR-NOT-007 | Canais externos como e-mail, SMS, WhatsApp, push e integrações de mensageria são capacidades futuras e dependem de fornecedor e política aprovados. | Futuro | MVP não envia comunicação externa automaticamente. |
| BR-NOT-008 | Estados de entrega, tentativa, falha, expiração e cancelamento devem ser rastreáveis, mas recibo de fornecedor não prova leitura ou compreensão pelo destinatário. | Futuro | Dashboard futuro distingue solicitação, entrega confirmada e falha sem afirmar leitura indevidamente. |
| BR-NOT-009 | Retentativas, limites de frequência, janela de silêncio, deduplicação e escalonamento devem ser definidos antes da produção. | Decisão pendente | Política define limite por destinatário/canal/evento e tratamento de falha permanente ou temporária. |
| BR-NOT-010 | Link de notificação para recurso protegido deve exigir autenticação e autorização atuais; não pode conceder acesso apenas pelo conhecimento do link. | Definida | Link enviado não permite consultar Appointment, File ou Patient sem credencial e Membership válidos. |
| BR-NOT-011 | Notificações devem gerar auditoria de solicitação, cancelamento e falha relevante, sem registrar conteúdo sensível ou credenciais do fornecedor. | Futuro | Evento registra Tenant, origem, canal, resultado e data/hora com metadados mínimos. |
| BR-NOT-012 | Notificações de emergência, prescrições, resultados clínicos, campanhas de marketing e comunicação em massa estão fora do MVP e exigem regras específicas. | Fora do MVP | MVP não trata canal de notificação como instrumento clínico, promocional ou de emergência. |

### 10.2 Casos de teste mínimos para evolução futura

- Evento do Tenant A não alcança destinatário do Tenant B.
- Falha de entrega não muda estado do domínio de origem.
- Template não expõe dados sensíveis desnecessários.
- Link de notificação não contorna autenticação ou autorização.
- Preferência e limites são aplicados antes do envio.
- Auditoria não registra conteúdo confidencial ou credenciais externas.

## 11. Integrações Externas

Integrações externas são capacidades futuras. Nenhum provedor externo pode enfraquecer isolamento de Tenant, autorização, rastreabilidade ou a fonte de verdade dos domínios internos.

### 11.1 Regras

| ID | Regra | Classificação | Critérios verificáveis |
|---|---|---|---|
| BR-INT-001 | Toda integração deve possuir finalidade, Tenant, dados envolvidos, responsável e escopo documentados antes de ser habilitada. | Decisão pendente | Não existe integração ativa sem registro de finalidade, dados e responsável. |
| BR-INT-002 | Credenciais, chaves, tokens e segredos de integrações são fornecidos por configuração segura e nunca ficam em código, logs ou respostas públicas. | Definida | Repositório, auditoria e logs não contêm segredo; falhas não o expõem. |
| BR-INT-003 | Credenciais e configurações específicas de Tenant devem permanecer isoladas e só ser usadas para operações daquele Tenant. | Definida | Integração configurada para A não é usada para enviar, buscar ou alterar dados de B. |
| BR-INT-004 | Dados enviados a provedor externo devem ser minimizados, autorizados e compatíveis com a finalidade aprovada. | Definida | Payload não inclui dado clínico, segredo ou informação de outro Tenant que não seja necessária. |
| BR-INT-005 | Integração não se torna fonte de verdade automática: mudanças recebidas só afetam domínio interno por fluxo validado e auditável. | Definida | Webhook ou sincronização não altera Patient, Appointment ou financeiro sem validação de origem, Tenant e regra de domínio. |
| BR-INT-006 | Webhooks devem validar autenticidade, integridade, idempotência, Tenant e tipo de evento antes de processamento. | Futuro | Evento inválido, repetido ou sem contexto confiável é rejeitado ou tratado sem duplicar efeito. |
| BR-INT-007 | Chamadas com efeito externo devem usar identificação idempotente ou mecanismo equivalente quando a operação puder ser repetida. | Futuro | Reenvio após timeout não cria cobrança, mensagem ou alteração externa duplicada. |
| BR-INT-008 | Falhas temporárias, timeout, indisponibilidade e retentativas devem seguir política explícita de limites, fila, backoff e monitoramento. | Decisão pendente | Política define tentativas, prazo, descarte, alerta e recuperação manual. |
| BR-INT-009 | Operações assíncronas de integração preservam Tenant, ator quando aplicável, correlação e autorização necessária durante toda execução. | Definida | Worker não usa contexto HTTP e não processa payload de A em contexto B. |
| BR-INT-010 | Solicitação, envio, recebimento, falha, retentativa e efeito relevante de integração devem gerar auditoria sem registrar segredos ou payload sensível completo. | Definida | Evento permite investigar origem, Tenant, provedor, resultado e correlação. |
| BR-INT-011 | Conectores com bancos, fiscal, pagamentos, convênios, mensageria, calendários ou plataformas clínicas são capacidades futuras e exigem especificação por provedor. | Futuro | MVP não depende de provedor externo para fluxos centrais. |
| BR-INT-012 | Integrações que envolvam dados de saúde, financeiro, comunicação ou transferência internacional exigem revisão de segurança, privacidade e requisitos jurídicos antes da produção. | Decisão pendente | Avaliação registra dados, risco, base aplicável, retenção e controles antes da ativação. |

### 11.2 Casos de teste mínimos para evolução futura

- Credencial de Tenant A nunca é usada em fluxo do B.
- Webhook inválido ou repetido não altera domínio interno.
- Timeout e retentativa não duplicam efeito externo.
- Payload não contém dados fora da finalidade aprovada.
- Falha não expõe segredo e gera evento técnico/auditável adequado.
- Job assíncrono preserva Tenant e correlação.

## Próximo passo: consolidar a Fase 2

A documentação de regras de negócio já cobre os domínios priorizados do MVP e as principais evoluções futuras. O próximo passo é revisar as **decisões pendentes**, fechar o catálogo inicial de permissões e transformar as regras do MVP em cenários de aceite e plano de implementação.

## Documentos relacionados

- [Requisitos Funcionais](requirements.md)
- [Casos de Uso](use-cases.md)
- [MVP](mvp.md)
- [Modelo de Domínio](domain-model.md)
- [Autenticação](../architecture/authentication.md)
- [Autorização](../architecture/authorization.md)
- [Segurança](../security/README.md)
- [Multi-Tenant](../multi-tenant/README.md)
