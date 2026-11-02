# Estado de implementação · Candidata 0.2
Data de referência: 01/11/2026. Esta página descreve a PR de remediação, sem afirmar merge, publicação ou uso em produção.

| Domínio | Código proposto | Verificação exigida |
|---|---|---|
| Identidade e sessão | Cadastro inicial, login, refresh rotacionado, logout, recuperação/reset, troca de instituição e permissões atuais | Testes de reuso, expiração, erro, revogação e entrega fictícia |
| Auditoria | Eventos transacionais de identidade e operações de negócio | Rollback e ausência de segredos |
| Vínculos | Convites, aceitação, perfis, suspensão/revogação e último administrador | Aceitação, permissão e proteção concorrente |
| Pacientes | Busca, cadastro, atualização, alerta de duplicidade, arquivo/reativação | Validação, isolamento e integridade |
| Recursos | Profissional/sala/equipamento, horários e bloqueios | Disponibilidade e reservas futuras |
| Agenda | Criação/alteração e ciclo de vida | Concorrência, intervalos consecutivos, papéis e isolamento |
| Arquivos | Conteúdo privado criptografado, inspeção e remoção lógica | MIME/estrutura, antimalware, quota e autorização |
| Relatórios/exportações | Pacientes, agenda e auditoria; CSV/PDF | Escopo, limites, geração e download após mudança de acesso |
| Interface | Fluxos de trabalho por instituição e permissão | Typecheck, build, navegador e smoke test conjunto |
| Operação | Contêineres, CI, inventário de dependências e runbook | Ambiente real, backup/restauração e observabilidade |

## Limites explícitos
- Recursos: até 100 por consulta; agenda: até 1.000 registros/93 dias; vínculos: até 1.000 nesta versão. Paginação ampliada é evolução necessária antes de exceder esses limites.
- Cadastro e login têm controles por origem; a topologia real do proxy precisa ser validada.
- E-mail depende de SMTP autenticado e URLs HTTPS. Arquivos dependem de chave externa e antimalware privado.
- Conteúdo privado fica criptografado no banco na primeira entrega, conforme ADR-0002.
- Não há prova de conformidade operacional nem autorização de uso de dados reais apenas pela existência desses recursos.

## Portão de produção
Exigir CI verde no commit final, validação dos cenários de aceite, dependências revisadas, proteção de branch compatível com o plano, HTTPS e segredos configurados, restauração testada e revisão do responsável pelo ambiente.
Financeiro, notificações e integrações externas continuam fora do MVP.

