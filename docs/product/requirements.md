# Requisitos Funcionais

Definição inicial dos requisitos funcionais do ORDIA.

## 1. Objetivo

Transformar a visão do Documento Mestre em comportamentos verificáveis do produto. Este documento define o que o ORDIA deve fazer, sem amarrar a implementação a uma tecnologia específica.

## 2. Atores

| Código | Ator | Responsabilidade |
|---|---|---|
| ACT-01 | Administrador do Tenant | Configura a organização e gerencia acesso |
| ACT-02 | Gestor | Acompanha operação e informações gerenciais |
| ACT-03 | Profissional | Executa atividades assistenciais/operacionais conforme seu perfil |
| ACT-04 | Recepção | Gerencia atendimento e agenda conforme permissão |
| ACT-05 | Financeiro | Executa operações financeiras autorizadas |
| ACT-06 | Auditor/Consulta | Acessa informações conforme escopo somente leitura |
| ACT-07 | Administrador da plataforma | Opera funções globais da plataforma, fora do escopo do Tenant comum |

Os papéis são uma proposta inicial. O modelo definitivo de permissões será refinado durante o desenho do domínio.

## 3. Requisitos por domínio

### 3.1 Identidade e acesso

**RF-ID-01** O sistema deve permitir autenticação de usuários.

**RF-ID-02** O sistema deve permitir encerramento de sessão.

**RF-ID-03** O sistema deve permitir recuperação de acesso conforme política de segurança definida.

**RF-ID-04** O sistema deve permitir ativação, desativação e gerenciamento de usuários por administradores autorizados.

**RF-ID-05** O sistema deve associar usuários a um contexto organizacional conforme as regras de tenancy.

**RF-ID-06** O sistema deve impedir acesso a funcionalidades não autorizadas.

### 3.2 Organização / Tenant

**RF-TEN-01** O sistema deve permitir o cadastro e configuração de uma organização.

**RF-TEN-02** O sistema deve manter configurações próprias de cada organização.

**RF-TEN-03** O sistema deve impedir que usuários acessem recursos de outro Tenant sem autorização explícita prevista pela plataforma.

**RF-TEN-04** O sistema deve permitir gerenciamento dos membros da organização conforme permissões.

### 3.3 Pacientes

**RF-PAT-01** Usuários autorizados devem poder cadastrar pacientes.

**RF-PAT-02** Usuários autorizados devem poder consultar pacientes do Tenant atual.

**RF-PAT-03** Usuários autorizados devem poder atualizar dados de pacientes.

**RF-PAT-04** O sistema deve manter histórico mínimo de alterações relevantes quando exigido pelo domínio.

**RF-PAT-05** O sistema deve evitar duplicidade indevida de pacientes conforme regras de negócio a serem definidas.

**RF-PAT-06** O acesso aos dados de pacientes deve respeitar permissões e contexto do Tenant.

### 3.4 Agenda

**RF-AGE-01** Usuários autorizados devem poder criar agendamentos.

**RF-AGE-02** O sistema deve permitir consulta de agenda por período e escopo autorizado.

**RF-AGE-03** O sistema deve permitir confirmação, alteração e cancelamento de agendamentos conforme regras de negócio.

**RF-AGE-04** O sistema deve relacionar o agendamento aos recursos necessários, como paciente, profissional e horário, quando aplicável.

**RF-AGE-05** O sistema deve reduzir conflitos de agenda por meio de validações de disponibilidade.

### 3.5 Financeiro

**RF-FIN-01** Usuários autorizados devem poder registrar informações financeiras suportadas pelo produto.

**RF-FIN-02** O sistema deve permitir consulta de informações financeiras conforme permissão.

**RF-FIN-03** Operações financeiras relevantes devem possuir rastreabilidade.

**RF-FIN-04** O acesso aos dados financeiros deve respeitar Tenant e autorização.

### 3.6 Relatórios

**RF-REP-01** O sistema deve disponibilizar relatórios definidos para o MVP.

**RF-REP-02** Relatórios devem respeitar o escopo de acesso do usuário.

**RF-REP-03** Exportações devem respeitar o contexto do Tenant e as permissões aplicáveis.

### 3.7 Arquivos

**RF-FIL-01** Usuários autorizados devem poder anexar arquivos aos recursos que suportarem anexos.

**RF-FIL-02** O sistema deve controlar acesso aos arquivos por Tenant e permissão.

**RF-FIL-03** O sistema deve registrar metadados necessários para localizar e administrar arquivos.

### 3.8 Auditoria

**RF-AUD-01** O sistema deve registrar eventos relevantes de segurança e administração.

**RF-AUD-02** Eventos de auditoria devem manter contexto suficiente para investigação.

**RF-AUD-03** O acesso à auditoria deve ser restrito a usuários autorizados.

## 4. Regras transversais

**RF-TR-01** Toda operação protegida deve validar autenticação.

**RF-TR-02** Toda operação protegida deve validar autorização no backend.

**RF-TR-03** Toda operação sobre recurso tenant-owned deve respeitar o Tenant Context.

**RF-TR-04** Dados sensíveis não devem ser retornados quando o usuário não possuir escopo adequado.

**RF-TR-05** Operações críticas devem possuir rastreabilidade quando aplicável.

## 5. Critérios de aceite gerais

Uma funcionalidade só deve ser considerada pronta quando, além do fluxo principal, possuir:

- validação de entrada;
- tratamento de erro;
- autorização;
- comportamento Multi-Tenant definido;
- testes para cenários relevantes;
- documentação quando a funcionalidade introduzir uma regra importante.

## 6. Fora do escopo do MVP

A princípio, não fazem parte do primeiro incremento obrigatório:

- microserviços;
- aplicativo mobile nativo;
- inteligência artificial como requisito central;
- marketplace;
- integrações com dezenas de sistemas externos;
- automações avançadas sem caso de uso validado;
- funcionalidades financeiras complexas que dependam de requisitos ainda não definidos.

Esses itens podem entrar futuramente mediante priorização.
