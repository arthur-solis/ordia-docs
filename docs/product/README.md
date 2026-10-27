# Produto

Documentação de definição funcional do ORDIA.

Esta área transforma a visão do Documento Mestre em requisitos, casos de uso, regras de negócio, modelo de domínio e escopo incremental de entrega.

## Documentos

- [Requisitos Funcionais](requirements.md)
- [Casos de Uso](use-cases.md)
- [MVP](mvp.md)
- [Modelo de Domínio](domain-model.md)
- [Regras de Negócio](business-rules.md)
- [Matriz de Acesso do MVP](access-control.md)
- [Cenários de Aceite do MVP](acceptance-criteria.md)
- [Decisões do MVP](mvp-decisions.md)

## Ordem de detalhamento das regras de negócio

1. **Identity & Access** — definido: identidade global, Membership, RBAC, autenticação, JWT/sessão, recuperação de senha, desativação e auditoria.
2. **Tenant & Organization** — definido: ciclo de vida, administração, Memberships, contexto organizacional, isolamento operacional e auditoria.
3. **Pacientes** — definido: cadastro, identificação, duplicidade, atualização, arquivamento, histórico e acesso.
4. **Agenda** — definido: recursos, disponibilidade, conflitos e ciclo de vida dos agendamentos.
5. **Arquivos & Anexos** — definido: armazenamento, vínculo, acesso, retenção e auditoria.
6. **Relatórios & Exportações** — definido: consultas agregadas, escopo, geração e entrega segura.
7. **Auditoria & Rastreabilidade** — definido: eventos, consulta segura, integridade e retenção.
8. **Profissionais & Recursos** — definido: capacidade, disponibilidade, estados e uso na Agenda.
9. **Financeiro** — definido como domínio futuro: lançamentos, estados, estornos e rastreabilidade.
10. **Notificações** — definido como domínio futuro: preferências, canais, entrega e privacidade.
11. **Integrações Externas** — definido como domínio futuro: provedores, webhooks, sincronização e falhas.

## Estado

**Fase 2 · Definição do produto**

A base de requisitos, casos de uso, MVP e modelo de domínio está consolidada. As regras de **Identity & Access**, **Tenant & Organization**, **Pacientes**, **Agenda**, **Arquivos & Anexos**, **Relatórios & Exportações**, **Auditoria & Rastreabilidade**, **Profissionais & Recursos** e os limites iniciais de **Financeiro** foram detalhados. A matriz de permissões, as decisões do MVP e os cenários de aceite estão consolidados. A Fase 2 está pronta para a Fase 3, sem que isso autorize o início de implementação neste momento.
