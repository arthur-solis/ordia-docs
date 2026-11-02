# Estado de implementação · MVP integrado para o TCC
Data de referência: 01/11/2026 (America/Cuiaba). A implementação foi integrada à main da aplicação pelo PR #3 e a documentação pelo PR #1. Isso registra integração de código, não implantação nem conclusão do TCC.

A prioridade atual é revisão funcional e visual, execução local, testes, documentação e demonstração com dados fictícios. Hospedagem e provedores externos serão avaliados após o TCC.

| Domínio | Código integrado | Validação a manter/completar |
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
- O código de e-mail usa SMTP; no TCC, a entrega pode ser capturada localmente. Esse ambiente e o tratamento dos links ainda precisam ser configurados, documentados e testados; não se presume que exista um modo local pronto.
- Arquivos exigem chave de criptografia e antimalware mesmo na demonstração local; não desabilitar essas validações.
- Conteúdo privado fica criptografado no banco na primeira entrega, conforme ADR-0002.
- Não há prova de conformidade operacional nem autorização de uso de dados reais apenas pela existência desses recursos.

## Pendências da entrega acadêmica
- Revisar telas, navegação, estados de erro/vazio/carregamento e responsividade.
- Validar as regras e permissões com os cenários de aceite e dados fictícios.
- Documentar o ambiente local e preparar roteiro de demonstração e evidências.
- Concluir o texto e os materiais acadêmicos conforme exigências da instituição.

Testes automatizados aprovados na integração são evidência técnica; não substituem a revisão visual e a validação da apresentação.

## Após o TCC · Portão de produção
Exigir CI verde no commit final, validação dos cenários de aceite, dependências revisadas, proteção de branch compatível com o plano, HTTPS e segredos configurados, restauração testada e revisão do responsável pelo ambiente.
Financeiro, notificações e integrações externas continuam fora do MVP.

