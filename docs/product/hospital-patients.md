# DEC-HOSP-002 · Cadastro e identificação de pacientes

Decisão de planejamento aprovada em 07/11/2026 para o [cenário hospitalar](hospital-scope.md). Ambulatório, pronto-socorro e internação usam a ficha do mesmo paciente dentro do hospital. O número interno identifica a ficha na instituição e permanece disponível mesmo quando o CPF não foi informado.

## Busca e cadastro normal

1. Antes de cadastrar, a recepção busca por nome, CPF ou número interno. A data de nascimento ajuda a distinguir pessoas com nomes iguais.
2. A ficha normal pede nome completo, data de nascimento e pelo menos um contato. O CPF é obrigatório quando o paciente tem CPF e o valor informado deve ser válido. Para quem não tem CPF, a equipe pode registrar outro documento, como passaporte.
3. Se o CPF já estiver cadastrado no hospital, a equipe confere a ficha existente antes de prosseguir. Confirmada a mesma pessoa, usa a ficha existente. Se a busca apontar apenas semelhança, como nome e data de nascimento, a recepção pode continuar após verificar que são pessoas distintas.

## Cadastro provisório no pronto-socorro

Se a pessoa chegar sem identificação ou sem os dados mínimos disponíveis, a equipe pode abrir uma ficha provisória com número interno e vincular o atendimento. Quando a identidade for confirmada, a equipe completa a ficha ou vincula o registro à ficha existente, preservando o histórico do atendimento.

O fluxo de conferência e vinculação, os campos mínimos provisórios e as permissões de regularização serão detalhados com o módulo de pronto-socorro. Uma sugestão de duplicidade exige conferência antes de vincular registros.

## Atualização e histórico

- A recepção pode corrigir dados cadastrais e contatos conforme autorização. Evoluções, diagnósticos e prescrições ficam no prontuário, com permissões próprias.
- Um perfil autorizado pode arquivar a ficha, preservando o histórico. Para um novo agendamento, a ficha precisa ser reativada.
- Convênio ou particular é registrado no atendimento. A mesma pessoa pode usar convênio em uma ocasião e pagar particular em outra, mantendo uma única ficha.

## Diferenças em relação à base integrada

A [decisão anterior do MVP](mvp-decisions.md#dec-mvp-006--patient-mínimo-e-duplicidade) descreve documento opcional e alerta de duplicidade, sem mesclagem. A nova regra de CPF no cadastro normal, o número interno como opção de busca e a ficha provisória com regularização são requisitos planejados para a evolução hospitalar. A documentação da API continua descrevendo o contrato da base até que o código seja ajustado e validado.

## Cenários para validar

- Cadastro normal de paciente com CPF válido e reutilização da ficha após confirmação de CPF já cadastrado.
- Cadastro normal de paciente sem CPF, com documento alternativo.
- Atendimento vinculado a ficha provisória e histórico preservado após confirmação de identidade.
- Paciente com um atendimento por convênio e outro particular usando a mesma ficha.
- Ficha arquivada com histórico consultável por pessoa autorizada, sem novo agendamento até reativação.
