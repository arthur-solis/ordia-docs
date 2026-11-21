# DEC-HOSP-003 · Profissionais e recursos

Decisão aprovada para o [cenário hospitalar](hospital-scope.md).

| Cadastro | Dados iniciais |
|---|---|
| Profissional | Nome, função, setor de atuação, disponibilidade e especialidade quando aplicável |
| Sala | Nome ou código, tipo, setor e horários de uso |
| Equipamento | Nome, código, localização e períodos disponíveis |

O cadastro profissional identifica quem pode ser reservado. A conta de usuário controla o acesso ao Ordia. Os dois registros podem ser vinculados conforme a função.

## Recursos compartilhados

- Cada sala ou equipamento tem um único cadastro e uma única agenda por instituição.
- O cadastro indica o setor de referência, a localização e os setores autorizados a reservar.
- Setores autorizados consultam a mesma disponibilidade. A permissão de reservar dá acesso aos horários livres e mantém protegidos os dados dos pacientes atendidos por outros setores.
- Cada recurso tem capacidade de uma reserva por intervalo. Se dois setores tentarem reservar o mesmo recurso no mesmo horário, apenas uma reserva pode ser confirmada.

## Disponibilidade

O recurso precisa estar ativo, dentro do horário de uso e livre de bloqueios e reservas sobrepostas. Férias, manutenção e interdição são bloqueios temporários. Quando deslocamento ou preparo exigirem tempo, o período também deve ficar indisponível.

Desativar um recurso preserva o histórico e impede novas reservas. A equipe resolve as reservas futuras antes da desativação. Leitos seguem o fluxo de ocupação da internação, com admissão, transferência e alta.

A base integrada já prevê recursos, horários e bloqueios. Setores autorizados, localização operacional e compartilhamento são regras da evolução hospitalar a implementar e validar. Veja [Agenda](hospital-agenda.md).
