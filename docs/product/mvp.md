# MVP do ORDIA

Definição do primeiro produto implementável do ORDIA.

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
- notificações simples, se necessárias ao fluxo validado.

## 4. Fora do MVP

- financeiro completo;
- faturamento complexo;
- integrações externas extensas;
- aplicativo mobile nativo;
- microserviços;
- IA como componente central;
- BI avançado;
- automações complexas;
- marketplace;
- funcionalidades cuja regra de negócio ainda não esteja definida.

Isso não significa que esses recursos não façam parte do futuro do ORDIA. Significa apenas que não devem bloquear a primeira entrega.

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

## 7. Sequência de implementação

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
- arquivos, se necessários;
- testes de integração;
- UX;
- segurança;
- documentação;
- preparação para staging.

## 8. Métrica de sucesso inicial

O MVP deve provar quatro coisas:

1. uma organização consegue operar no ORDIA;
2. seus usuários possuem acessos diferentes conforme suas permissões;
3. seus dados permanecem isolados de outros Tenants;
4. os fluxos centrais de paciente e agenda funcionam de ponta a ponta.

Se essas quatro condições forem atendidas, a plataforma terá uma fundação adequada para receber os demais domínios.
