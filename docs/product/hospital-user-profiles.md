# Perfis hospitalares e responsabilidades
Base aprovada em 03/11/2026. Acesso somente por funcionários autorizados.

| ID | Perfil | Responsabilidade planejada |
|---|---|---|
| PH-01 | Administrador do hospital | Configurar instituição, setores, usuários e acessos |
| PH-02 | Gestor hospitalar | Acompanhar operação, indicadores e relatórios |
| PH-03 | Recepção | Cadastrar pacientes, agendar e registrar chegada |
| PH-04 | Equipe de internação e leitos | Organizar admissões, ocupação, transferências e saída administrativa |
| PH-05 | Médico | Registrar atendimento, evoluções, diagnósticos, prescrições e solicitações |
| PH-06 | Enfermeiro | Registrar avaliações e cuidados de enfermagem e acompanhar pacientes/equipe |
| PH-07 | Técnico de enfermagem | Registrar cuidados e checagens conforme atribuições e autorização |
| PH-08 | Farmácia | Controlar medicamentos, estoque, dispensação e devoluções |
| PH-09 | Laboratório e diagnóstico por imagem | Acompanhar solicitações e registrar etapas/resultados conforme função |
| PH-10 | Equipe do centro cirúrgico | Organizar programação, salas, equipe, materiais e registros do setor |
| PH-11 | Estoque e almoxarifado | Controlar materiais, entradas, saídas e reposição |
| PH-12 | Convênios e autorizações | Conferir dados de cobertura e acompanhar pedidos de autorização |
| PH-13 | Faturamento | Preparar contas hospitalares e acompanhar cobranças aos convênios |
| PH-14 | Financeiro e caixa | Registrar pagamentos, recebimentos, despesas e pendências |
| PH-15 | Auditor | Consultar registros e contas dentro de escopo autorizado |

## Limites desta definição
Os PH são perfis funcionais de planejamento, não roles já implementadas nem novas permissões concedidas pelo código. A [matriz de acesso existente](access-control.md) descreve a base integrada; o mapeamento dos PH para permissões será detalhado por módulo.
Uma pessoa poderá acumular perfis conforme suas funções. Setor e instituição contextualizam o trabalho, sem conceder acesso automaticamente.
Administrar o sistema não implica acesso irrestrito ao prontuário. A recepção não obtém acesso clínico apenas por consultar o cadastro de um paciente. Auditoria também exige finalidade e escopo autorizado.
Laboratório e imagem podem exigir especializações de perfil; a separação detalhada ainda será validada. A lista não substitui definição de atribuições profissionais.

## Referências
- [Cenário e abrangência](hospital-scope.md)
- [Telas e navegação](screen-map-navigation.md)
