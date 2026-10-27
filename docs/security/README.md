# Segurança

Segurança é requisito estrutural do ORDIA. Autenticação, autorização, isolamento de Tenant e validações críticas são sempre responsabilidades do backend.

## Controles do MVP

- Spring Security + JWT com access token de 15 minutos e refresh token rotacionado.
- Validação atual de usuário, Tenant, Membership e permission em cada operação protegida.
- Rate limit e resposta genérica para login e recuperação de senha.
- Hash seguro para senhas, refresh, convite e recuperação; nunca registrar segredos.
- Escopo de Tenant em banco, API, cache, jobs, arquivos e exportações.
- Auditoria de acessos e operações críticas, sem dados sensíveis desnecessários.
- Arquivos privados com autorização revalidada e entrega temporária quando aplicável.
- Segredos exclusivamente por configuração segura do ambiente.

## Ameaças a cobrir

Acesso anônimo, elevação de privilégio, acesso cruzado entre Tenants, manipulação de IDs/filtros, reutilização de token, automação abusiva, upload malicioso, vazamento de segredos e falhas de isolamento em tarefas assíncronas.

## Privacidade e LGPD

A [operação de privacidade do MVP](privacy-mvp.md) define classificação, minimização, retenção provisória, backups/restauração, solicitações de titulares e resposta a incidentes. Ela requer validação jurídica antes de produção.

## Checklist para cada recurso

- [ ] Autenticação e permission validadas no backend.
- [ ] Tenant Context aplicado a leitura e escrita.
- [ ] Entrada, limite de payload e erro seguro tratados.
- [ ] Logs sem senha, token, segredo ou dado sensível desnecessário.
- [ ] Eventos relevantes auditados.
- [ ] Testes de acesso indevido e isolamento presentes.
