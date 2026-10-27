# Arquitetura do Frontend

## Stack

- SvelteKit
- TypeScript
- Tailwind CSS

## Organização

O frontend deve acompanhar os domínios do produto, mantendo componentes visuais reutilizáveis separados da lógica específica de cada módulo.

```text
frontend/
└── src/
    ├── routes/
    ├── lib/
    │   ├── auth/
    │   ├── tenancy/
    │   ├── patients/
    │   ├── scheduling/
    │   ├── billing/
    │   └── shared/
    ├── components/
    │   ├── ui/
    │   ├── forms/
    │   ├── tables/
    │   └── layouts/
    └── services/
```

## Responsabilidades

### Routes

Define páginas, layouts e navegação da aplicação.

### Lib por domínio

Contém lógica específica de cada área funcional, como estado, tipos, validações de interface e adaptadores necessários ao frontend.

### Components

Contém componentes reutilizáveis, priorizando composição e consistência visual.

### Services

Centraliza comunicação com a API e outros serviços externos utilizados pelo frontend.

## TypeScript

TypeScript será utilizado como linguagem principal do frontend para fornecer tipagem estática, contratos explícitos e maior segurança durante a evolução do código.

Os tipos de API devem ser mantidos alinhados aos contratos OpenAPI sempre que possível.

## Segurança

O frontend pode ocultar funcionalidades sem permissão para melhorar a experiência, mas isso nunca deve ser considerado mecanismo de segurança.

A autorização definitiva pertence ao backend.

## Performance

O frontend deve priorizar:

- carregamento eficiente;
- divisão adequada de código;
- redução de chamadas desnecessárias;
- componentes reutilizáveis;
- uso consciente de estado global;
- otimização de imagens e arquivos;
- experiência responsiva em desktop, tablet e smartphone.

## Acessibilidade

A interface deve ser construída considerando navegação por teclado, semântica HTML, contraste, feedback de estado e compatibilidade com tecnologias assistivas.
