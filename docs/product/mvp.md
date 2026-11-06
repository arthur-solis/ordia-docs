# MVP da base integrada do ORDIA

Definição do núcleo do ORDIA para o TCC. A base já está integrada à main; as prioridades abaixo organizam a revisão e a demonstração, sem afirmar conclusão acadêmica.



## Ampliação hospitalar aprovada
A [visão hospitalar](hospital-scope.md) amplia o planejamento para hospital geral privado, com convênios e particulares e acesso apenas de funcionários. Este documento descreve a base anterior; não especifica integralmente pronto-socorro, internação, prontuário, enfermagem, farmácia, exames, centro cirúrgico ou faturamento hospitalar. Financeiro integra a visão do produto; implementação e recorte demonstrável do TCC serão definidos por etapas.

## 1. Objetivo do MVP

Entregar um núcleo funcional que prove as bases mais importantes do ORDIA: identidade, Multi-Tenant, controle de acesso, cadastro de pacientes e agenda.

O MVP não deve tentar representar todo o sistema de gestão hospitalar de uma vez. A prioridade é construir uma fundação real, utilizável e tecnicamente sólida.

## 2. Princípio de priorização

A ordem considera:

1. dependências estruturais;
2. valor operacional;
3. risco técnico e de segurança;
4. capacidade de validar o produto rapidamente.

## 3. Escopo do MVP

### P0 · Fundação

- autenticação;
- usuários;
- Tenant/organização;
- membership e papéis;
- autorização;
- auditoria mínima;
- configurações básicas da organização.

### P1 · Operação central

- cadastro de pacientes;
- busca e visualização de pacientes;
- agenda;
- criação, confirmação, alteração e cancelamento de agendamentos;
- profissionais/recursos necessários para agenda.

### P2 · Apoio à operação

- arquivos/anexos;
- dashboard operacional básico;
- relatórios básicos;
- recuperação de acesso e convites, com possibilidade de captura de e-mail local para demonstração.

## 4. Fora da base integrada atual

- todo o domínio financeiro, inclusive lançamentos simples;
- notificações gerais e integrações externas de negócio;
- faturamento complexo;
- integrações externas extensas;
- aplicativo mobile nativo;
- microserviços;
- IA como componente central;
- BI avançado;
- automações complexas;
- marketplace;
- funcionalidades cuja regra de negócio ainda não esteja definida.

Financeiro/faturamento e demais áreas hospitalares passaram a integrar a visão aprovada. A lista acima descreve os limites da base existente, não uma exclusão definitiva do TCC. A seleção das próximas entregas será feita por módulo.

## 5. Fluxo mínimo demonstrável

O primeiro incremento deve permitir demonstrar:

```text
Criar organização
       ↓
Criar administrador
       ↓
Autenticar
       ↓
Configurar organização
       ↓
Criar usuário/equipe
       ↓
Cadastrar paciente
       ↓
Criar agendamento
       ↓
Consultar agenda
       ↓
Alterar/cancelar agendamento
       ↓
Registrar auditoria
```

O fluxo deve funcionar respeitando Tenant e permissões em todas as etapas.

## 6. Critérios de pronto do MVP

O MVP não será considerado concluído apenas porque os fluxos de tela funcionam.

Deve existir, no mínimo:

- autenticação funcional;
- autorização no backend;
- isolamento Multi-Tenant testado;
- persistência transacional;
- API documentada;
- tratamento consistente de erros;
- validação de entrada;
- testes dos fluxos críticos;
- logs adequados;
- auditoria mínima;
- configuração reproduzível do ambiente;
- documentação atualizada.

## 7. Sequência de referência para implementação e revisão

A base dessas etapas já foi integrada. Use a sequência para estudar, revisar e validar os módulos; não representa uma lista de desenvolvimento ainda não iniciado. Hospedagem e operação externa são etapas posteriores ao TCC.

### Sprint 0 · Base

- projeto backend;
- projeto frontend;
- banco;
- Docker/desenvolvimento;
- migrations;
- configuração de ambientes;
- observabilidade mínima.

### Sprint 1 · Identity + Tenancy

- usuário;
- Tenant;
- membership;
- roles;
- login;
- JWT;
- autorização;
- contexto de Tenant.

### Sprint 2 · Pacientes

- entidade paciente;
- cadastro;
- consulta;
- atualização;
- validações;
- testes de isolamento.

### Sprint 3 · Agenda

- profissionais/recursos;
- disponibilidade;
- agendamento;
- estados;
- conflitos;
- confirmação/cancelamento.

### Sprint 4 · Operação e acabamento

- dashboard básico;
- auditoria;
- validação dos arquivos/anexos já implementados;
- testes de integração;
- UX;
- segurança;
- documentação;
- preparação do ambiente local e roteiro de apresentação do TCC.

## 8. Métrica de sucesso inicial

O MVP deve provar quatro coisas:

1. uma organização consegue operar no ORDIA;
2. seus usuários possuem acessos diferentes conforme suas permissões;
3. seus dados permanecem isolados de outros Tenants;
4. os fluxos centrais de paciente e agenda funcionam de ponta a ponta.

Se essas quatro condições forem atendidas, a plataforma terá uma fundação adequada para receber os demais domínios.
