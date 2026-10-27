# Cenários de Aceite do MVP

Cenários verificáveis para validar o comportamento do MVP antes da implementação e durante os testes de integração.

## AC-01 · Criar organização e administrador

**Dado** um usuário elegível para iniciar uma organização  
**Quando** a organização é criada  
**Então** o sistema cria um Tenant `ACTIVE`, um Membership `ACTIVE` e a role `TENANT_ADMIN` para o administrador inicial  
**E** registra auditoria da criação.

## AC-02 · Isolamento entre Tenants

**Dado** um usuário com Membership ativo no Tenant A  
**Quando** tenta consultar ou alterar recurso do Tenant B por ID, filtro, rota ou payload  
**Então** a operação é negada sem expor dados ou confirmar a existência do recurso.

## AC-03 · Gerir membros

**Dado** um `TENANT_ADMIN` no Tenant atual  
**Quando** convida ou ativa um membro  
**Então** o Membership inicia em `PENDING` e só opera após `ACTIVE`  
**E** a alteração é auditada.

## AC-04 · Proteção do último administrador

**Dado** um Tenant `ACTIVE` com somente um administrador ativo  
**Quando** alguém tenta revogar, suspender ou remover sua capacidade administrativa  
**Então** a operação é negada.

## AC-05 · Autorização por role

**Dado** um usuário `RECEPTION`  
**Quando** tenta concluir Appointment ou arquivar Patient  
**Então** a operação é negada.  
**Quando** cria ou confirma Appointment permitido  
**Então** a operação é aceita no Tenant atual.

## AC-06 · Cadastro de Patient

**Dado** um usuário com `patient:create`  
**Quando** envia cadastro com campos obrigatórios e formato válido  
**Então** o Patient é criado como `ACTIVE` no Tenant atual  
**E** possíveis duplicidades são sinalizadas antes da confirmação.  
**Quando** os dados são inválidos  
**Então** nenhum registro parcial é persistido.

## AC-07 · Arquivamento de Patient

**Dado** um Patient `ACTIVE`  
**Quando** usuário autorizado o arquiva  
**Então** o Patient não pode receber novo Appointment  
**E** seu histórico permanece consultável por quem tiver autorização.

## AC-08 · Disponibilidade e conflito

**Dado** um recurso `ACTIVE` de capacidade unitária  
**Quando** existe Appointment `SCHEDULED` ou `CONFIRMED` no intervalo solicitado  
**Então** um novo Appointment sobreposto é negado, inclusive em tentativas concorrentes.  
**E** intervalos consecutivos não entram em conflito.

## AC-09 · Ciclo de vida do Appointment

**Dado** Appointment `SCHEDULED`  
**Quando** usuário autorizado confirma, cancela, conclui ou marca ausência  
**Então** somente as transições permitidas são aceitas  
**E** estados terminais não são reabertos diretamente.

## AC-10 · Arquivos protegidos

**Dado** um File associado a recurso do Tenant A  
**Quando** usuário do Tenant B usa o ID, uma URL ou chave de armazenamento conhecida  
**Então** o download é negado.  
**Quando** usuário autorizado remove o File  
**Então** a remoção é lógica e o evento é auditado.

## AC-11 · Relatório e exportação

**Dado** usuário com `report:export`  
**Quando** solicita exportação autorizada  
**Então** o job preserva Tenant, solicitante e filtros.  
**Quando** seu Membership é suspenso antes do download  
**Então** a entrega é negada.

## AC-12 · Auditoria

**Dado** uma ação relevante de negócio ou segurança  
**Quando** ela é executada  
**Então** o sistema registra ator/contexto, Tenant, recurso, ação, resultado e data/hora  
**Sem** registrar senha, token completo, segredo ou conteúdo sensível desnecessário.

## Gate de pronto do MVP

O MVP está apto a avançar quando todos os cenários acima possuírem testes automatizados de integração e nenhum cenário de isolamento ou autorização estiver falhando.

## Documentos relacionados

- [Matriz de Acesso do MVP](access-control.md)
- [Regras de Negócio](business-rules.md)
- [MVP](mvp.md)
