# DEC-HOSP-005 · Equipe e permissões

Decisão aprovada para o ambiente único do Ordia. A TI de cada hospital gerencia convites e vínculos seguindo o [fluxo de acesso](hospital-access.md).

## Concessão de acesso

O perfil define as ações permitidas. A instituição e o setor definem onde elas podem ser executadas. A TI atribui perfis e setores aos funcionários e pode suspender ou revogar vínculos.

Uma pessoa pode acumular perfis com escopos distintos. Quem é Recepção no Ambulatório e Gestão em Exames pode agendar no Ambulatório e administrar recursos em Exames. O perfil de gestão em Exames não amplia o acesso no Ambulatório.

| Perfil | Ações no escopo autorizado |
|---|---|
| TI do hospital | Gerenciar convites, vínculos, perfis e setores da própria instituição. Acesso ao prontuário exige permissão própria. |
| Recepção | Buscar e cadastrar pacientes, agendar, confirmar, remarcar, cancelar e registrar ausência. |
| Profissional assistencial | Consultar sua agenda e concluir atendimentos sob sua responsabilidade, conforme o perfil. |
| Gestão do setor | Configurar horários, bloqueios e recursos sob responsabilidade do setor. |
| Auditoria | Consultar os registros autorizados em modo de leitura. |

## Verificações

- O servidor valida a ação e o escopo em cada operação, inclusive em acessos por link direto.
- Mudanças de perfil e setor são auditadas. A instituição mantém pelo menos um administrador ativo.
- Suspender ou revogar o vínculo interrompe o acesso à instituição.
- Reservar um recurso compartilhado exige autorização para o setor. A disponibilidade compartilhada preserva os dados dos pacientes de outros setores.

Esta é a regra aprovada para o planejamento hospitalar. A [matriz do MVP](access-control.md) continua descrevendo os papéis e permissões da base integrada. O detalhamento de todas as permissões por módulo e a autorização por setor ainda precisam de implementação e validação.
