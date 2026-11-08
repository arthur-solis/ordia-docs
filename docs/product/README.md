# Produto

Documentação de definição funcional do ORDIA.

Esta área transforma a visão do Documento Mestre em requisitos, casos de uso, regras de negócio, modelo de domínio e escopo incremental de entrega.

## Documentos

- [Cenário hospitalar e visão do produto](hospital-scope.md)
- [Perfis hospitalares e responsabilidades](hospital-user-profiles.md)
- [Mapa inicial de telas e navegação](screen-map-navigation.md)
- [Acesso ao Ordia](hospital-access.md)
- [Cadastro e identificação de pacientes](hospital-patients.md)

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
9. **Financeiro** — incluído na visão hospitalar; implementação a planejar: lançamentos, estados, estornos e rastreabilidade.
10. **Notificações** — definido como domínio futuro: preferências, canais, entrega e privacidade.
11. **Integrações Externas** — definido como domínio futuro: provedores, webhooks, sincronização e falhas.

## Estado

O núcleo foi implementado e integrado à main. A etapa atual é consolidar a entrega do TCC: revisar regras e telas, detalhar navegação e estados da interface, validar execução local e reunir evidências. Consulte o [estado de implementação](implementation-status.md) e o [MVP](mvp.md).

A visão agora abrange gestão hospitalar administrativa e assistencial, incluindo financeiro/faturamento. A base implementada é um subconjunto; requisitos completos e recorte de demonstração do TCC serão definidos progressivamente. Notificações gerais e integrações externas continuam sem implementação planejada nesta etapa. Produção será avaliada após o TCC.
