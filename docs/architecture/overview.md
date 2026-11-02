# Visão Arquitetural

## Objetivo

Definir a visão estrutural do ORDIA e estabelecer as principais fronteiras entre cliente, aplicação, dados e infraestrutura.

## Estilo arquitetural

O ORDIA será iniciado como um **Modular Monolith**.

Isso significa que a aplicação backend será implantada inicialmente como uma unidade, mas internamente será dividida em módulos de domínio com responsabilidades e fronteiras bem definidas.

A distribuição física em múltiplos serviços poderá ocorrer futuramente, mas não deve ser introduzida apenas por preferência tecnológica.

## Princípios

1. **Modularidade antes de distribuição**
2. **Baixo acoplamento**
3. **Alta coesão por domínio**
4. **Segurança desde a entrada da requisição**
5. **Multi-Tenant como requisito estrutural**
6. **Infraestrutura substituível quando possível**
7. **Observabilidade desde o crescimento inicial**
8. **Complexidade proporcional à necessidade real**

## Fluxo principal

```text
Navegador → SvelteKit → API Spring Boot → MySQL
               UI       regras/segurança   dados e conteúdo criptografado
```

## Fronteiras

### Frontend

Responsável por apresentação, navegação, experiência do usuário, estado de interface e comunicação com a API.

### API

Responsável por autenticação, autorização, validação, contratos HTTP e entrada das operações do sistema.

### Application

Responsável pela execução dos casos de uso e coordenação entre domínio e infraestrutura.

### Domain

Responsável pelas regras de negócio que definem o comportamento do ORDIA.

### Infrastructure

Responsável por persistência, cache, armazenamento de objetos, integrações externas e demais detalhes tecnológicos.

## Regra de dependência

As regras de negócio não devem depender diretamente de detalhes externos como HTTP, banco de dados ou serviços de armazenamento.

A direção desejada é:

```text
API → Application → Domain
                 ↓
          Infrastructure
```

As dependências concretas devem ser controladas para evitar que detalhes de infraestrutura contaminem o domínio.

## Evolução futura

A arquitetura deve permitir que módulos com fronteiras maduras sejam extraídos posteriormente sem exigir uma reconstrução completa da aplicação.

A extração de serviços será tratada como decisão arquitetural independente e registrada em ADR quando ocorrer.

## Recorte do TCC e evolução

O diagrama representa o MVP atual: identidade, organizações/membros, pacientes, recursos, agenda, arquivos, relatórios e auditoria. Financeiro é futuro. Redis e S3/compatível não são dependências da implementação atual. Consulte a [decisão de conteúdo privado](../decisions/ADR-0002-private-content-mvp.md).

A prioridade é a demonstração local com dados fictícios. Hospedagem externa e operação em produção serão avaliadas após o TCC.
