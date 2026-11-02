# Autenticação
Referência da implementação 0.2 integrada à main. A autenticação é própria da aplicação; não exige contratação de provedor externo para o TCC.

## Identidade e sessão
Access JWT de até 15 minutos; refresh de até 30 dias em família, sem renovação além da expiração original.
JWT contém sub, tenant_id, membership_id, session_family, jti, iat e exp. Roles/permissões são consultadas no banco; não ficam congeladas no token.
Cada requisição revalida User, Tenant e Membership ACTIVE, correspondência de IDs, sessão e permissões atuais.
Login escolhe vínculo elegível em Tenant ativo; troca explícita valida o destino e emite outra sessão.

## Rotação e logout
Somente hashes de refresh são persistidos. Renovar consome o token anterior e cria sucessor.
Reusar token já rotacionado revoga toda a família e registra evento. Logout revoga a família, atingindo access/refresh associados.
Reset revoga todas as famílias do usuário. Alterações de estado/permissão têm efeito na próxima validação.
Tokens legados sem família continuam válidos apenas até sua expiração original, sem renovação.

## Proteção de login
Até 5 tentativas por identificador/origem em 15 minutos, bloqueio de 15 minutos. Sucesso limpa a contagem daquele par.
Há limite adicional por origem e controle do cadastro. Reservas de tentativas em andamento contam para prevenir corrida.
Resposta de credencial é genérica e a verificação de conta desconhecida também executa o hash de senha.
O endereço de origem não é aceito de headers livres. O servidor da interface pode encaminhá-lo com autenticação HMAC e janela curta, mediante segredo externo compartilhado e ingress confiável.

## Recuperação e convite
Recuperação: 3 solicitações por hora por identificador/origem; token de uso único e validade de 30 minutos.
A fila persiste referência da conta; o worker gera o token, guarda hash e envia por SMTP/STARTTLS.
Identificadores existentes/inexistentes têm a mesma resposta pública. Com e-mail desabilitado, ambos retornam 503.
Convite tem validade de 7 dias; conta existente exige senha atual para aceitar, sem substituição silenciosa de credencial.
Nenhum token em claro entra em banco, log ou URL de query. Links usam fragmento removido pela interface.

## Navegador
A interface usa servidor intermediário na mesma origem. Tokens ficam em cookies HttpOnly/Secure/SameSite Strict e não em localStorage.
Mutações validam Origin; downloads não são públicos. Renovação entre abas usa Web Locks quando disponível.
