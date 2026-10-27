# Casos de Uso

Casos de uso prioritários do ORDIA, derivados dos requisitos funcionais iniciais.

## UC-01 · Autenticar usuário

**Ator:** usuário

**Objetivo:** acessar o ambiente autorizado do ORDIA.

**Fluxo principal:**

1. Usuário informa credenciais.
2. Sistema valida identidade.
3. Sistema determina o contexto organizacional disponível.
4. Sistema cria a sessão/token conforme a política de segurança.
5. Usuário acessa o ambiente permitido.

**Exceções:** credenciais inválidas, usuário inativo, contexto inválido ou acesso não autorizado.

## UC-02 · Configurar organização

**Ator:** administrador do Tenant

**Objetivo:** configurar dados e preferências da organização.

**Fluxo:**

1. Administrador acessa configurações.
2. Sistema valida permissão.
3. Administrador altera dados permitidos.
4. Sistema valida os valores.
5. Sistema persiste alterações.
6. Sistema registra auditoria quando aplicável.

## UC-03 · Gerenciar usuários

**Ator:** administrador do Tenant

**Objetivo:** administrar membros da organização.

**Fluxo:**

1. Administrador abre gerenciamento de usuários.
2. Sistema apresenta somente usuários do escopo permitido.
3. Administrador cria, altera, ativa, desativa ou ajusta acesso.
4. Sistema valida permissões.
5. Sistema registra alterações relevantes.

## UC-04 · Cadastrar paciente

**Ator:** profissional ou recepção autorizados

**Objetivo:** criar um paciente no Tenant atual.

**Fluxo:**

1. Usuário inicia cadastro.
2. Sistema valida campos obrigatórios.
3. Sistema verifica possíveis duplicidades conforme regra definida.
4. Usuário confirma.
5. Sistema cria paciente associado ao Tenant atual.
6. Sistema retorna o paciente criado.

## UC-05 · Consultar paciente

**Ator:** usuário autorizado

**Objetivo:** localizar e visualizar dados de paciente.

**Fluxo:**

1. Usuário realiza busca.
2. Sistema aplica Tenant Context.
3. Sistema aplica permissões.
4. Sistema retorna somente recursos acessíveis.

## UC-06 · Criar agendamento

**Ator:** recepção ou profissional autorizado

**Objetivo:** reservar um horário para um paciente.

**Fluxo:**

1. Usuário seleciona paciente.
2. Seleciona profissional/recurso, quando aplicável.
3. Seleciona data e horário.
4. Sistema verifica disponibilidade.
5. Sistema cria o agendamento.
6. Sistema registra evento de domínio relevante.

## UC-07 · Confirmar ou cancelar agendamento

**Ator:** usuário autorizado

**Objetivo:** atualizar o estado de um agendamento.

**Fluxo:**

1. Usuário acessa agendamento.
2. Sistema valida escopo e permissão.
3. Usuário solicita alteração.
4. Sistema valida transição de estado.
5. Sistema atualiza o agendamento.
6. Sistema registra evento/auditoria quando aplicável.

## UC-08 · Registrar operação financeira

**Ator:** financeiro ou usuário autorizado

**Objetivo:** registrar uma operação financeira suportada pelo produto.

**Fluxo:**

1. Usuário inicia operação.
2. Sistema valida permissão.
3. Usuário informa dados.
4. Sistema valida regras.
5. Sistema persiste a operação.
6. Sistema registra rastreabilidade.

## UC-09 · Gerar relatório

**Ator:** gestor ou usuário autorizado

**Objetivo:** obter informação consolidada dentro do escopo permitido.

**Fluxo:**

1. Usuário escolhe relatório.
2. Sistema valida permissão.
3. Sistema aplica Tenant Context e filtros autorizados.
4. Sistema processa dados.
5. Sistema apresenta ou disponibiliza resultado.

## UC-10 · Anexar arquivo

**Ator:** usuário autorizado

**Objetivo:** associar arquivo a um recurso suportado.

**Fluxo:**

1. Usuário seleciona arquivo.
2. Sistema valida tamanho e tipo.
3. Sistema verifica permissão.
4. Sistema armazena objeto.
5. Sistema persiste metadados.
6. Sistema disponibiliza o arquivo somente dentro do escopo autorizado.

## UC-11 · Consultar auditoria

**Ator:** administrador/auditor autorizado

**Objetivo:** investigar eventos relevantes.

**Fluxo:**

1. Usuário abre auditoria.
2. Sistema valida permissão.
3. Sistema aplica escopo organizacional.
4. Sistema retorna eventos autorizados.

## UC-12 · Trocar contexto organizacional

**Ator:** usuário vinculado a mais de um Tenant, caso essa capacidade seja habilitada.

**Objetivo:** operar em outro contexto permitido sem misturar dados.

**Fluxo:**

1. Usuário solicita mudança de Tenant.
2. Sistema valida membership.
3. Sistema estabelece novo Tenant Context.
4. Sessão/contexto passa a operar no novo escopo.
5. Dados e permissões são recalculados conforme o Tenant atual.

## Regra transversal dos casos de uso

Nenhum caso de uso tenant-owned pode confiar apenas em IDs enviados pelo cliente. A autorização e o escopo devem ser determinados e validados pelo backend.
