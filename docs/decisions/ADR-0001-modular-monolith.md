# ADR-0001: Adoção de Modular Monolith como arquitetura inicial

- **Status:** Accepted
- **Data:** 2026-09-03
- **Decisão:** Adotar Modular Monolith como arquitetura inicial do ORDIA.

## Contexto

O ORDIA é uma plataforma SaaS de gestão para instituições de saúde, projetada para operar em modelo Multi-Tenant e crescer em funcionalidades, usuários e volume de dados.

O sistema ainda está em fase de estruturação. Nesse estágio, a prioridade é estabelecer fronteiras de domínio sólidas, segurança, testabilidade, manutenção simples e capacidade de evolução.

## Problema

É necessário escolher uma arquitetura que permita crescimento sem introduzir complexidade operacional desnecessária no início do projeto.

Microserviços poderiam oferecer isolamento e escala independente, porém também adicionariam custos de infraestrutura, observabilidade, deploy, comunicação distribuída, consistência, testes e operação.

## Decisão

O backend será desenvolvido inicialmente como um **Modular Monolith**.

A aplicação será implantada como uma unidade, mas organizada internamente em módulos de domínio independentes e com fronteiras explícitas.

Estrutura conceitual:

```text
br/com/ordia/
├── identity/
├── tenancy/
├── patient/
├── scheduling/
├── billing/
├── reporting/
├── files/
└── shared/
```

Cada módulo seguirá, quando aplicável, a separação:

```text
api/
application/
domain/
infrastructure/
```

A arquitetura deve preservar a possibilidade de extração futura de módulos para serviços independentes quando uma necessidade concreta justificar essa mudança.

## Alternativas consideradas

### Microservices desde o início

**Não adotado.**

A complexidade distribuída não é justificada pelo estágio atual do produto. O custo operacional seria antecipado antes de existir uma necessidade comprovada de distribuição.

### Monólito sem modularização

**Não adotado.**

Embora simples inicialmente, tende a permitir alto acoplamento entre funcionalidades e dificulta a evolução futura do sistema.

### Serverless como arquitetura principal

**Não adotado.**

Não oferece vantagem suficiente para justificar a escolha como arquitetura principal neste estágio e não está alinhado à stack oficial definida para o backend.

## Consequências positivas

- Menor complexidade operacional inicial.
- Deploy mais simples.
- Comunicação interna de baixa latência.
- Transações mais simples quando necessárias.
- Desenvolvimento e debugging facilitados.
- Fronteiras de domínio preparadas para futura distribuição.
- Menor quantidade de infraestrutura para operar inicialmente.

## Consequências negativas

- Módulos compartilham o mesmo processo de execução.
- Escala inicialmente ocorre no nível da aplicação.
- Falhas graves no processo podem afetar múltiplos módulos.
- Extração futura exigirá trabalho de engenharia.
- Fronteiras modulares precisam ser protegidas por disciplina arquitetural e testes.

## Regras decorrentes

1. Não criar microserviços apenas por antecipação.
2. Não permitir dependências indiscriminadas entre módulos.
3. Registrar decisões que alterem significativamente as fronteiras arquiteturais.
4. Projetar módulos com contratos claros.
5. Priorizar isolamento lógico antes de isolamento físico.
6. Considerar extração de serviço somente quando houver justificativa técnica ou de negócio.

## Critérios para revisar esta decisão

Esta ADR poderá ser revisada quando houver evidências de que um ou mais módulos precisam de:

- escala independente;
- isolamento de falhas;
- ciclo de deploy independente;
- requisitos tecnológicos incompatíveis com o restante da aplicação;
- processamento ou integração de alta complexidade;
- autonomia operacional claramente definida.
