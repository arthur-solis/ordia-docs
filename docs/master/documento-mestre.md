# Documento Mestre ORDIA

**Versão:** 1.0.0  
**Status:** Em desenvolvimento  
**Classificação:** Documento oficial  
**Origem:** consolidação e adaptação do Documento Mestre original do projeto  
**Última atualização:** setembro de 2026

---

## Controle de versões

| Versão | Data | Alteração |
|---|---|---|
| 1.0.0 | Setembro/2026 | Migração e reestruturação do Documento Mestre para o ORDIA |

---

# Sumário

1. [Introdução](#1-introdução)
2. [Visão geral](#2-visão-geral)
3. [Missão, visão e valores](#3-missão-visão-e-valores)
4. [Objetivos](#4-objetivos)
5. [Escopo do produto](#5-escopo-do-produto)
6. [Modelo SaaS e Multi-Tenant](#6-modelo-saas-e-multi-tenant)
7. [Tecnologias oficiais](#7-tecnologias-oficiais)
8. [Princípios de desenvolvimento](#8-princípios-de-desenvolvimento)
9. [Diretrizes arquiteturais](#9-diretrizes-arquiteturais)
10. [Domínios e módulos](#10-domínios-e-módulos)
11. [Requisitos não funcionais](#11-requisitos-não-funcionais)
12. [Segurança](#12-segurança)
13. [Documentação e decisões](#13-documentação-e-decisões)
14. [Roadmap inicial](#14-roadmap-inicial)
15. [Regras absolutas do projeto](#15-regras-absolutas-do-projeto)
16. [Histórico e evolução](#16-histórico-e-evolução)

---

# 1. Introdução

Este documento estabelece a visão oficial do **ORDIA** e consolida suas principais definições de produto, arquitetura, tecnologia e engenharia.

Ele deve funcionar como uma fonte central de referência para decisões relevantes do projeto. Documentos especializados podem detalhar assuntos específicos, mas não devem contradizer as definições estabelecidas aqui sem que a alteração seja registrada.

Toda mudança estrutural, arquitetural ou tecnológica relevante deverá ser documentada antes ou durante sua implementação, conforme o processo definido no repositório.

## 1.1 O que é o ORDIA

O ORDIA é uma **plataforma web SaaS destinada à gestão de instituições da área da saúde**, como clínicas, consultórios, empresas e organizações relacionadas ao setor.

A plataforma tem como objetivo centralizar processos de gestão em um ambiente único, moderno e escalável, oferecendo uma experiência organizada para as organizações e seus usuários.

Desde sua concepção, o ORDIA é orientado por:

- Escalabilidade
- Segurança
- Performance
- Organização
- Modularidade
- Manutenibilidade
- Experiência do usuário

---

# 2. Visão geral

O ORDIA foi concebido para ser uma plataforma de longo prazo, capaz de evoluir continuamente sem exigir uma reconstrução completa de sua base tecnológica a cada nova etapa.

A arquitetura deverá permitir que centenas ou milhares de organizações utilizem a mesma plataforma de forma independente, mantendo seus ambientes e dados logicamente isolados.

Cada organização deve perceber o ORDIA como seu próprio ambiente de trabalho, mesmo utilizando uma infraestrutura compartilhada.

O produto deverá buscar equilíbrio entre três dimensões fundamentais:

1. **Experiência:** interface clara, rápida e intuitiva.
2. **Engenharia:** arquitetura organizada, modular e sustentável.
3. **Confiabilidade:** segurança, isolamento, consistência e observabilidade.

---

# 3. Missão, visão e valores

## 3.1 Missão

Simplificar a gestão da área da saúde utilizando tecnologia moderna, arquitetura robusta e excelente experiência para o usuário.

## 3.2 Visão

Ser reconhecido como uma das melhores plataformas de gestão em saúde do Brasil.

## 3.3 Valores

- Qualidade
- Organização
- Escalabilidade
- Performance
- Segurança
- Confiabilidade
- Inovação
- Código limpo
- Arquitetura bem definida
- Documentação completa

---

# 4. Objetivos

O ORDIA deverá buscar os seguintes objetivos:

- Ser moderno.
- Ser rápido e responsivo.
- Ser visualmente consistente e agradável.
- Ser intuitivo.
- Ser escalável.
- Ser confiável.
- Ser fácil de manter.
- Ser preparado para evolução contínua.
- Centralizar processos de gestão em um único ambiente.
- Manter isolamento rigoroso entre organizações.

Os objetivos acima são direcionadores do produto e devem ser considerados nas decisões de arquitetura e implementação.

---

# 5. Escopo do produto

## 5.1 Natureza do sistema

O ORDIA será um **Software as a Service (SaaS)** acessado pela web.

Não deverá existir dependência de instalação local para utilização normal da plataforma. O acesso será realizado por meio de navegador.

## 5.2 Dispositivos suportados

A interface deverá ser projetada para funcionar adequadamente em:

- Desktop
- Notebook
- Tablet
- Smartphone

## 5.3 Escopo funcional inicial

O conceito original do projeto prevê um ambiente por organização contendo, entre outros possíveis módulos:

- Gestão da organização
- Usuários
- Permissões
- Configurações
- Pacientes
- Agendamentos
- Financeiro
- Relatórios
- Arquivos
- Logs

A existência desses domínios no Documento Mestre não significa que todos devam ser implementados simultaneamente. A priorização será definida pelo roadmap e pelos requisitos funcionais de cada fase.

---

# 6. Modelo SaaS e Multi-Tenant

O **Multi-Tenant** é uma característica fundamental do ORDIA.

Cada organização cadastrada na plataforma será tratada como um **Tenant**.

Cada Tenant deverá possuir seu próprio contexto lógico, incluindo, conforme os módulos utilizados:

- Organização
- Usuários
- Papéis e permissões
- Configurações
- Pacientes
- Agendamentos
- Dados financeiros
- Relatórios
- Arquivos
- Logs e registros de auditoria

## 6.1 Regra fundamental de isolamento

> Uma organização nunca poderá acessar informações pertencentes a outra organização.

Essa regra é **absoluta** e deve ser aplicada em todas as camadas relevantes do sistema.

O isolamento não deve depender exclusivamente da interface. A arquitetura, o backend, as consultas ao banco de dados, as APIs, os mecanismos de autorização e os processos assíncronos deverão considerar o contexto do Tenant.

## 6.2 Princípio de segurança

Toda nova funcionalidade deverá responder explicitamente à seguinte pergunta:

**Como o contexto do Tenant será identificado, validado e protegido nesta funcionalidade?**

Nenhum módulo deverá ser considerado concluído enquanto seu comportamento Multi-Tenant não estiver definido.

---

# 7. Tecnologias oficiais

A stack oficial definida para o projeto é:

## 7.1 Frontend

- **SvelteKit**
- **TypeScript**
- **Tailwind CSS**

## 7.2 Backend

- **Java**
- **Spring Boot**
- **Spring Security**
- **JWT**

## 7.3 Banco de dados

- **MySQL** como banco atualmente definido.

A possibilidade de utilização futura de PostgreSQL ou MongoDB poderá ser avaliada mediante análise técnica. Uma alteração de tecnologia deverá ser tratada como decisão arquitetural, e não como mudança casual de implementação.

## 7.4 Cache

- **Redis**

## 7.5 Documentação de API

- **OpenAPI**
- **Swagger**

## 7.6 Armazenamento

- **Amazon S3 ou armazenamento compatível com S3**

## 7.7 Regra da stack

A stack oficial representa a base tecnológica aprovada para o projeto. Substituições deverão ser justificadas tecnicamente e registradas como decisão arquitetural antes de se tornarem oficiais.

---

# 8. Princípios de desenvolvimento

## 8.1 Clean Code

O código deverá priorizar clareza, legibilidade e facilidade de manutenção.

## 8.2 SOLID

Os princípios SOLID deverão ser aplicados sempre que contribuírem para uma arquitetura mais coesa, testável e sustentável.

## 8.3 Separação de responsabilidades

Cada camada e componente deverá possuir responsabilidade clara.

No backend, a arquitetura inicial deverá considerar a separação entre conceitos como:

- Controllers
- Services
- Repositories
- Entities
- DTOs
- Configurações
- Segurança

A estrutura poderá evoluir para outros padrões quando necessário, desde que a separação de responsabilidades seja preservada.

## 8.4 Componentização

Componentes deverão ser reutilizáveis quando houver uma responsabilidade comum real. A reutilização não deverá ser forçada apenas para reduzir quantidade de arquivos.

## 8.5 Padronização

Deverá existir consistência na nomenclatura de:

- Arquivos
- Pastas
- Classes
- Interfaces
- Métodos
- Rotas
- Endpoints
- Variáveis
- Componentes

## 8.6 Performance

Desempenho deverá ser considerado durante o projeto e não apenas depois que problemas surgirem.

## 8.7 Segurança desde o início

Segurança não será tratada como complemento posterior. Cada funcionalidade deverá ser projetada considerando autenticação, autorização, validação, exposição de dados e isolamento de Tenant quando aplicável.

## 8.8 Documentação

Funcionalidades importantes, decisões arquiteturais e módulos complexos deverão possuir documentação correspondente.

---

# 9. Diretrizes arquiteturais

A arquitetura do ORDIA deverá privilegiar:

- Baixo acoplamento entre módulos.
- Alta coesão dentro de cada módulo.
- Separação clara entre apresentação, domínio e infraestrutura quando aplicável.
- Componentização e reutilização responsáveis.
- Evolução incremental.
- Testabilidade.
- Observabilidade.
- Segurança por padrão.
- Isolamento Multi-Tenant.

A arquitetura detalhada será mantida em [`docs/architecture/`](../architecture/README.md).

Decisões que alterem significativamente a arquitetura deverão ser registradas em [`docs/decisions/`](../decisions/README.md).

---

# 10. Domínios e módulos

Os módulos abaixo representam o mapa inicial do produto e não devem ser interpretados como uma especificação funcional completa.

| Domínio | Responsabilidade inicial |
|---|---|
| Organização | Dados e configurações da organização/Tenant |
| Identidade | Usuários, autenticação e identidade |
| Autorização | Papéis, permissões e controle de acesso |
| Pacientes | Gestão dos pacientes e seus dados |
| Agenda | Agendamentos, disponibilidade e horários |
| Financeiro | Processos e informações financeiras |
| Relatórios | Consultas, indicadores e relatórios |
| Arquivos | Armazenamento e gerenciamento de arquivos |
| Auditoria | Logs, rastreabilidade e eventos relevantes |
| Configurações | Preferências e parâmetros da organização |

Cada domínio deverá possuir documentação própria quando sua complexidade justificar.

---

# 11. Requisitos não funcionais

O ORDIA deverá considerar os seguintes requisitos não funcionais como parte de sua definição arquitetural:

## RNF01. Segurança

Os dados deverão ser protegidos contra acesso não autorizado.

## RNF02. Isolamento Multi-Tenant

Dados de diferentes organizações não poderão ser expostos entre si.

## RNF03. Escalabilidade

A arquitetura deverá permitir crescimento de usuários, organizações e volume de dados sem dependência de uma reestruturação completa do sistema.

## RNF04. Performance

Operações críticas deverão ser projetadas para apresentar resposta adequada e evitar processamento desnecessário.

## RNF05. Disponibilidade e confiabilidade

A infraestrutura e a aplicação deverão ser projetadas para minimizar falhas e permitir recuperação adequada.

## RNF06. Manutenibilidade

O código e a arquitetura deverão permanecer compreensíveis e modificáveis conforme o projeto cresça.

## RNF07. Responsividade

A interface deverá funcionar adequadamente nos dispositivos definidos no escopo.

## RNF08. Observabilidade

O sistema deverá possuir mecanismos adequados para identificar falhas, acompanhar comportamento e investigar eventos relevantes.

---

# 12. Segurança

A segurança é um requisito estrutural do ORDIA.

A documentação detalhada deverá ser mantida em [`docs/security/`](../security/README.md).

Os principais eixos previstos são:

- Autenticação
- Autorização
- JWT e gestão de sessão
- Controle de acesso baseado em papéis e permissões
- Isolamento Multi-Tenant
- Validação de entrada
- Proteção de dados
- Auditoria
- Logs de segurança
- Gestão segura de arquivos
- Proteção das APIs

Nenhuma funcionalidade deverá presumir que a interface do frontend seja uma barreira de segurança suficiente. Toda autorização relevante deverá ser validada no backend.

---

# 13. Documentação e decisões

O repositório do ORDIA é a fonte central de documentação do projeto.

A documentação está organizada por áreas para evitar que o Documento Mestre se transforme em um arquivo impossível de manter.

## 13.1 Documento Mestre

Define a visão geral e as regras de alto nível do projeto.

## 13.2 Documentação arquitetural

Detalha a arquitetura e as decisões técnicas estruturais.

## 13.3 Documentação de segurança

Concentra requisitos e mecanismos relacionados à segurança.

## 13.4 Documentação Multi-Tenant

Define como o isolamento entre organizações será implementado e validado.

## 13.5 Documentação de API

Define contratos, padrões e convenções da API.

## 13.6 ADRs

Decisões arquiteturais relevantes deverão ser registradas como **Architecture Decision Records**.

O Documento Mestre não deverá acumular cada detalhe técnico. Quando uma decisão exigir histórico, alternativas, consequências e justificativa, ela deverá possuir um ADR próprio e ser referenciada quando necessário.

---

# 14. Roadmap inicial

## Fase 1. Fundação

- [x] Definir identidade do projeto como ORDIA
- [x] Estruturar repositório
- [x] Estruturar documentação
- [ ] Consolidar requisitos do produto
- [ ] Consolidar Documento Mestre

## Fase 2. Arquitetura

- [ ] Definir arquitetura geral
- [ ] Definir modelo de domínio
- [ ] Definir estratégia Multi-Tenant detalhada
- [ ] Definir autenticação
- [ ] Definir autorização
- [ ] Definir RBAC/permissões
- [ ] Definir padrões de API
- [ ] Definir modelo de dados
- [ ] Definir estratégia de arquivos
- [ ] Definir observabilidade

## Fase 3. Fundação técnica

- [ ] Estruturar backend
- [ ] Estruturar frontend
- [ ] Configurar banco de dados
- [ ] Configurar Redis
- [ ] Configurar armazenamento S3 ou compatível
- [ ] Configurar ambientes
- [ ] Configurar CI/CD

## Fase 4. Primeiro produto funcional

- [ ] Autenticação
- [ ] Gestão de organizações
- [ ] Gestão de usuários
- [ ] Permissões
- [ ] Primeiro módulo de negócio
- [ ] Auditoria básica
- [ ] Documentação da API

## Fase 5. Evolução

- [ ] Expansão dos módulos de negócio
- [ ] Relatórios
- [ ] Financeiro
- [ ] Arquivos
- [ ] Observabilidade avançada
- [ ] Otimizações de performance
- [ ] Escalabilidade horizontal conforme necessidade

O roadmap é evolutivo e poderá ser alterado mediante novas decisões de produto e engenharia.

---

# 15. Regras absolutas do projeto

As seguintes regras constituem princípios obrigatórios do ORDIA:

1. **Multi-Tenant é obrigatório.**
2. **Uma organização nunca poderá acessar dados de outra organização.**
3. **Segurança deve ser considerada desde a criação de cada funcionalidade.**
4. **Código deve permanecer organizado e compreensível.**
5. **A arquitetura deve preservar separação de responsabilidades.**
6. **Componentes reutilizáveis devem ser priorizados quando houver reutilização real.**
7. **Performance deve ser considerada antes da conclusão de funcionalidades críticas.**
8. **Documentação deve acompanhar a evolução do sistema.**
9. **Decisões arquiteturais importantes devem ser registradas.**
10. **Alterações relevantes da stack devem possuir justificativa técnica e registro.**
11. **Nenhuma funcionalidade deve ignorar o contexto do Tenant.**
12. **Regras de segurança não devem depender exclusivamente do frontend.**

---

# 16. Histórico e evolução

O ORDIA é a evolução do projeto anteriormente denominado **Aurea Health**. O Documento Mestre original foi criado em julho de 2026 e estabelecia a visão inicial de uma plataforma SaaS de gestão para instituições da área da saúde.

Durante a evolução do projeto, a identidade foi consolidada como **ORDIA**, e a documentação foi reorganizada para separar visão de produto, arquitetura, segurança, Multi-Tenant, API e decisões arquiteturais.

Esta versão preserva os fundamentos do documento original, ao mesmo tempo em que transforma suas definições em uma estrutura documental mais adequada para o crescimento do projeto.

## 16.1 Próxima evolução documental

As próximas versões deverão aprofundar principalmente:

- Requisitos funcionais detalhados.
- Modelo de domínio.
- Arquitetura geral.
- Modelo Multi-Tenant.
- Autenticação e autorização.
- RBAC.
- Contratos de API.
- Modelo de dados.
- Diagramas arquiteturais.
- Fluxos críticos.
- ADRs.

---

> **Estado atual:** o Documento Mestre define a direção oficial do ORDIA. Detalhes de implementação deverão ser mantidos nos documentos especializados correspondentes.
