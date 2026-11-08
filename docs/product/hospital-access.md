# DEC-HOSP-001 · Acesso ao Ordia

Decisão de planejamento aprovada em 07/11/2026 para o [cenário hospitalar](hospital-scope.md). A base de login, vínculos e convites já existe. O fluxo de implantação e a demonstração abaixo ainda precisam ser validados.

## Criação da instituição e primeiro administrador

1. O operador do Ordia cria a instituição (tenant) e envia um convite ao primeiro responsável da TI do hospital com o perfil de administrador daquela instituição.
2. O responsável aceita o convite e ativa seu vínculo. Se for seu primeiro acesso ao Ordia, define a própria senha. Se já tiver conta, autentica-se com a senha existente.
3. A TI do hospital passa a convidar funcionários, atribuir os perfis autorizados e suspender ou revogar vínculos dentro da própria instituição.

O operador do Ordia e a TI atribuem acesso por convite. Cada pessoa é responsável pela própria senha. A permissão para administrar contas e perfis é distinta das permissões de acesso ao prontuário.

## Convite de funcionário

1. Em **Equipe → Convidar funcionário**, a TI informa o e-mail e seleciona os perfis autorizados, como Recepção.
2. O Ordia envia o link por e-mail e exibe o convite como **Pendente**. O vínculo ainda não autoriza acesso ao hospital.
3. A pessoa abre o link, confere a instituição e aceita. Ela define a senha se estiver criando a primeira conta ou usa a senha existente se já tiver conta.
4. O vínculo passa para **Ativo**. A pessoa pode entrar no painel com os acessos atribuídos.

O link é de uso único e tem prazo. A TI pode reenviar se expirar. A política da base está em [Decisões do MVP](mvp-decisions.md#dec-mvp-004--convite-e-membership).

## Login e gestão de acesso

- Funcionários entram com e-mail e senha. Com um único hospital elegível, seguem ao painel. Com mais de um, escolhem a instituição em que vão trabalhar. A seleção inicial de instituição é comportamento planejado a conferir com a base.
- Na recuperação, o funcionário solicita um link e define uma nova senha.
- Suspender ou revogar o vínculo interrompe o acesso àquele hospital, inclusive em sessões abertas. Vínculos ativos com outras instituições continuam sujeitos às próprias permissões.
- O ambiente é único e as áreas aparecem conforme instituição, setor e permissões. Veja o [mapa de navegação](screen-map-navigation.md).

## Demonstração do TCC

Preparar localmente um hospital fictício e o primeiro administrador da TI. Demonstrar a TI convidando alguém da recepção, a abertura do e-mail em uma caixa de teste local, a aceitação, a definição da senha e o primeiro login com o perfil de Recepção. Conferir se a pessoa acessa apenas as áreas autorizadas.

Ficam para detalhamento a interface de provisionamento pelo operador e a configuração reproduzível da captura local de e-mails.
