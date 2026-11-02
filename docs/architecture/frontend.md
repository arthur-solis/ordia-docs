# Frontend
A base integrada usa SvelteKit 3, Svelte 5, TypeScript e servidor Node 24, com CSS próprio responsivo.
A interface inclui login/cadastro/recuperação, pacientes, recursos e disponibilidade, agenda, equipe, relatórios/exportações, auditoria e configuração da instituição.

## Segurança
O navegador fala somente com a mesma origem. O servidor encaminha chamadas à API privada e mantém access/refresh em cookies HttpOnly.
Permissões orientam a navegação; o backend continua responsável por cada decisão de acesso.
Não persistir dados clínicos ou tokens em armazenamento local. Limpar sessão na saída e não manter cache de respostas.
Fusos são apresentados pela instituição; horários inexistentes/ambíguos por mudança de fuso são recusados no formulário.

## Validação
Typecheck, build e Playwright em CI. Testes de interface usam servidor fictício isolado com dados demonstrativos.
Os testes HTTP com MySQL verificam os serviços de domínio; há fluxo de navegador com API real na validação da integração. O ambiente local da apresentação ainda precisa ser executado e conferido.
Para o TCC ainda é necessário revisar o mapa de telas, os campos/ações, os estados de interface e os protótipos; a compilação não representa aprovação visual. A demonstração ocorre localmente com dados fictícios. Produção será avaliada após o TCC.
