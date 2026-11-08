# DEC-HOSP-004 · Agenda

Decisão aprovada para consultas e exames marcados. A chegada espontânea no pronto-socorro segue a entrada e a triagem.

## Criar e remarcar

1. A recepção seleciona um paciente ativo, um profissional, o setor, a duração e os recursos exigidos pelo atendimento. Sala e equipamento são selecionados quando necessários.
2. O Ordia oferece horários em que todos os recursos selecionados estão disponíveis para o setor autorizado.
3. Ao salvar, o servidor revalida permissões, disponibilidade e conflitos. Se o horário acabou de ser reservado, informa o conflito para que a recepção escolha outro.
4. Na remarcação, a reserva original continua válida até que a nova seja confirmada pelo sistema. Uma tentativa recusada mantém o horário e os recursos anteriores.

| Ação | Resultado | Responsável |
|---|---|---|
| Agendar | Cria a reserva com estado **Agendado** | Recepção autorizada |
| Confirmar | Muda para **Confirmado** e mantém os recursos | Recepção autorizada |
| Remarcar | Atualiza horário ou recursos após nova validação | Recepção autorizada |
| Cancelar | Muda para **Cancelado**, libera a reserva e mantém o histórico | Recepção autorizada |
| Concluir | Muda para **Concluído** após o atendimento | Equipe assistencial autorizada |
| Registrar ausência | Muda para **Ausência** quando o paciente não comparece | Recepção autorizada |

Agendamentos cancelados, concluídos ou com ausência preservam o histórico. Um novo atendimento requer novo agendamento. A base mantém as regras de transição em [Regras de negócio](business-rules.md).

## Cenários de validação

- Consulta ou exame com profissional, sala e equipamento só é oferecido quando todos estão livres.
- Dois setores autorizados tentam reservar o mesmo ultrassom no mesmo horário. Uma reserva é confirmada e a outra recebe conflito.
- Remarcação para um horário ocupado mantém a reserva original.
- Cancelamento torna o intervalo disponível se os demais critérios forem atendidos.
- Recepção pode registrar ausência. Conclusão exige permissão assistencial.

A base já possui agendamentos e checagem de conflito. O fluxo de seleção por setor e as novas regras de compartilhamento precisam ser validados como parte da evolução hospitalar.
