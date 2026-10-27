# Escalabilidade

## Estratégia inicial

O ORDIA será projetado para escalar horizontalmente o backend quando necessário, mantendo a aplicação o mais stateless possível.

```text
                    ┌── ORDIA API #1 ──┐
Client → Load Balancer ├── ORDIA API #2 ──┼→ MySQL
                    └── ORDIA API #N ──┘   Redis
                                             S3
```

## Princípios

- Evitar estado de sessão preso a uma única instância.
- Externalizar dados compartilhados quando necessário.
- Utilizar cache com critérios claros.
- Monitorar gargalos antes de otimizar.
- Priorizar índices e consultas eficientes.
- Manter operações idempotentes quando apropriado.
- Processar tarefas demoradas de forma assíncrona quando houver necessidade real.

## Modular Monolith como base

A modularização permite escalar o sistema sem assumir imediatamente a complexidade operacional de microserviços.

Um módulo poderá ser candidato à extração quando demonstrar fronteira de domínio madura e uma necessidade concreta de distribuição.

## Critérios para extração de serviço

Uma extração deve considerar:

1. necessidade de escala independente;
2. isolamento de falhas;
3. implantação independente;
4. requisitos tecnológicos específicos;
5. integrações externas complexas;
6. autonomia clara do domínio;
7. custo operacional aceitável.

## Performance

Performance é requisito arquitetural e deve ser acompanhada por métricas reais.

Não devem ser introduzidas tecnologias de infraestrutura apenas por expectativa de escala futura.

## Observabilidade

A capacidade de escalar deve ser acompanhada por observabilidade suficiente para identificar:

- latência;
- throughput;
- erros;
- saturação de recursos;
- consultas lentas;
- utilização de cache;
- falhas de integrações.
