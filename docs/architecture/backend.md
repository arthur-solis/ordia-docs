# Arquitetura do Backend

## Stack

- Java
- Spring Boot
- Spring Security
- JWT
- MySQL
- Redis
- S3 ou armazenamento compatível

## Organização por domínio

O backend será organizado preferencialmente por **feature/domain**, evitando uma estrutura global baseada apenas em tipos técnicos.

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

Cada módulo poderá conter:

```text
module/
├── api/
├── application/
├── domain/
└── infrastructure/
```

## API

A camada `api` expõe os contratos externos da aplicação.

Responsabilidades:

- Controllers
- DTOs de entrada e saída
- Validação de requests
- Mapeamento de respostas HTTP
- Tratamento padronizado de erros

Controllers não devem concentrar regras de negócio complexas.

## Application

A camada `application` implementa casos de uso e coordena operações.

Exemplos:

- Criar paciente
- Confirmar agendamento
- Criar cobrança
- Desativar usuário

Casos de uso devem receber dados já validados estruturalmente e executar as regras necessárias do domínio.

## Domain

A camada `domain` concentra o comportamento de negócio.

Pode conter:

- Entidades
- Value Objects
- Regras de negócio
- Domain Services
- Domain Events
- Interfaces necessárias ao domínio

O domínio não deve depender diretamente de Spring MVC, banco de dados ou APIs externas.

## Infrastructure

A camada `infrastructure` implementa detalhes técnicos necessários pela aplicação.

Exemplos:

- Repositórios MySQL
- Configuração Redis
- Clientes S3
- Integrações externas
- Implementações de interfaces do domínio

## Shared

`shared` deve conter apenas componentes realmente transversais, como abstrações comuns, erros base ou utilidades justificadas.

Não utilizar `shared` como atalho para evitar definir a qual domínio uma funcionalidade pertence.

## Transações

Operações que alteram múltiplos recursos relacionados devem possuir limites transacionais explícitos.

A definição do limite da transação pertence à camada de aplicação, enquanto o mecanismo transacional permanece como detalhe de infraestrutura/framework.

## Tratamento de erros

A API deve possuir uma representação consistente de erros, evitando expor stack traces ou detalhes internos.

Erros esperados de negócio devem ser distinguíveis de falhas inesperadas de infraestrutura.

## Testabilidade

A separação entre API, aplicação, domínio e infraestrutura deve permitir testes independentes.

Prioridade inicial:

1. Testes de regras de domínio
2. Testes de casos de uso
3. Testes de integração de persistência
4. Testes de API
5. Testes ponta a ponta para fluxos críticos
