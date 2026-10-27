# Decisões do MVP

Decisões de produto e segurança fechadas para permitir a implementação do núcleo do ORDIA. As políticas podem evoluir em ADRs quando trouxerem impacto arquitetural adicional.

## DEC-MVP-001 · Sessão e tokens

- Access token JWT: validade de **15 minutos**.
- Refresh token: validade máxima de **30 dias**, com rotação a cada renovação.
- Logout, desativação de User, suspensão/revogação de Membership e alteração de senha invalidam o refresh token ativo.
- Tokens continuam sujeitos à validação de User, Tenant, Membership e permission atuais no backend.

## DEC-MVP-002 · Proteção de login

- Máximo de **5 tentativas falhas** por identificador e origem em janela de **15 minutos**.
- Ao exceder o limite, novas tentativas ficam bloqueadas por **15 minutos**.
- Resposta pública é genérica e não enumera contas.
- Rate limiting e eventos de falha são obrigatórios; CAPTCHA não integra o MVP.

## DEC-MVP-003 · Recuperação de senha

- Link de uso único, válido por **30 minutos**.
- Nova solicitação invalida o link anterior.
- Limite de **3 solicitações por hora** por identificador e origem.
- Após redefinição, refresh tokens ativos são invalidados.

## DEC-MVP-004 · Convite e Membership

- Convite é enviado por e-mail e gera Membership `PENDING`.
- Link de convite é único, expira em **7 dias** e pode ser cancelado ou reenviado.
- Aceitação ativa o Membership somente quando o User está `ACTIVE`.
- Novo convite é obrigatório após Membership `REVOKED`.

## DEC-MVP-005 · Tenant Context

- Access token carrega o Tenant Context atual.
- Troca de Tenant exige endpoint autenticado, Membership `ACTIVE` no destino e emissão de novo par de tokens.
- O backend valida Tenant Context em toda operação tenant-owned; ID de Tenant do cliente nunca é suficiente.

## DEC-MVP-006 · Patient mínimo e duplicidade

- Campos mínimos: nome completo, data de nascimento e ao menos um meio de contato.
- Documento é opcional no MVP, mas, se informado, deve ser válido conforme tipo configurado.
- Possível duplicidade é alertada por documento normalizado quando presente; caso contrário, por nome normalizado + data de nascimento.
- Duplicidade alerta, não bloqueia, e não há mesclagem no MVP.

## DEC-MVP-007 · Recursos e agenda

- MVP suporta recursos `PROFESSIONAL`, `ROOM` e `EQUIPMENT`.
- Um Appointment exige Patient ativo e ao menos um `PROFESSIONAL` ativo.
- Salas e equipamentos são opcionais por Appointment.
- Todos os recursos do MVP têm capacidade unitária.
- Horário é armazenado em UTC; o Tenant define timezone de exibição.
- Horários de trabalho e bloqueios são definidos por recurso; fora deles não há disponibilidade.
- Cancelamento, confirmação, conclusão e ausência não exigem motivo no MVP, mas são auditados.

## DEC-MVP-008 · Arquivos e exportações

- Tipos permitidos: PDF, JPEG e PNG.
- Limite: **10 MB** por arquivo e **10 arquivos** por recurso proprietário.
- Exportações aceitam CSV e PDF, com validade de **24 horas** após conclusão.
- Download sempre revalida autorização; arquivos e exportações não são públicos.

## DEC-MVP-009 · Auditoria

- Operações críticas falham quando a auditoria transacional obrigatória não puder ser persistida.
- Retenção padrão será definida antes de produção; o MVP preserva eventos sem exclusão por interface.
- Logs técnicos permanecem separados de auditoria.

## DEC-MVP-010 · Relatórios do MVP

- Catálogo inicial: agenda por período, Patients ativos/arquivados e eventos de auditoria autorizados.
- Relatórios respeitam a mesma matriz de permissões das consultas de origem.
- Limite padrão de exportação: **10.000 linhas** e **5 jobs ativos por Tenant**.

## Fora desta decisão

Financeiro, notificações e integrações externas permanecem futuros e exigem decisões próprias antes de implementação.
