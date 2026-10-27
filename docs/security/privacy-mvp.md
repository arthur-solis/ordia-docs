# Privacidade e LGPD Operacional do MVP

Este documento converte a preocupação de privacidade em práticas do produto. Não substitui orientação jurídica nem a definição formal de papéis, bases legais ou prazos pela organização responsável.

## 1. Inventário e classificação

| Classe | Exemplos | Controle mínimo |
|---|---|---|
| Público | marca e documentação pública | sem dados pessoais. |
| Interno | configuração técnica e métricas agregadas | acesso restrito por função. |
| Pessoal | nome, e-mail, telefone, data de nascimento de usuário/paciente | Tenant, permissão, TLS e logs sem conteúdo sensível. |
| Sensível/alto impacto | documentos anexos e qualquer informação de saúde futura | armazenamento privado, mínimo privilégio, auditoria de acesso e revisão antes de ampliar escopo. |
| Segredo | senha, token, chave e credencial | hash ou cofre; nunca em logs, respostas ou commits. |

O MVP não deve introduzir prontuário clínico, diagnóstico ou dados de saúde adicionais sem revisão específica de privacidade.

## 2. Finalidade e minimização

- Coletar apenas os dados necessários para operação do Tenant, atendimento administrativo e Agenda.
- Campos opcionais continuam opcionais; a ausência de documento não impede o cadastro quando a regra funcional permitir.
- Exportações devem conter somente os campos necessários ao relatório solicitado.
- Dados pessoais não devem ser colocados em URL, métricas, nomes de arquivo público ou logs de aplicação.

## 3. Acesso e compartilhamento

- O Tenant é a fronteira primária de acesso.
- O backend valida usuário ativo, Membership ativa e permission em cada operação protegida.
- Fornecedores de infraestrutura só recebem o acesso estritamente necessário e devem ser registrados antes do uso em produção.
- Arquivos e exports são privados; downloads usam autorização revalidada e URL temporária quando aplicável.

## 4. Retenção e descarte

Enquanto uma política jurídica formal não for aprovada:

- Pacientes, usuários e arquivos usam arquivamento/remoção lógica; não há limpeza automática irreversível no MVP.
- Eventos de auditoria são preservados e não possuem exclusão pela interface.
- Tokens expirados e sessões revogadas podem ser eliminados por rotina técnica após sua utilidade de segurança, com registro da execução.
- Toda nova rotina de eliminação exige prazo aprovado, avaliação de backups e teste de restauração.

A definição de prazos legais por categoria é uma decisão pendente anterior ao uso em produção.

## 5. Backups e restauração

- Backups devem ser criptografados, possuir acesso mínimo e retenção documentada.
- A restauração deve ocorrer em ambiente isolado, com acesso registrado.
- Antes de produção, executar e registrar teste de restauração ao menos trimestralmente.
- Uma solicitação de eliminação deve considerar que cópias em backup expiram por sua política; não se edita backup histórico individualmente sem procedimento aprovado.

## 6. Solicitações do titular

O fluxo mínimo é:

1. receber a solicitação por canal definido;
2. confirmar identidade e vínculo antes de revelar dados;
3. registrar a solicitação e o responsável;
4. localizar dados no Tenant correto;
5. submeter acesso, correção, anonimização ou eliminação à revisão jurídica/operacional;
6. executar somente o que for aprovado e auditar o resultado.

A aplicação não expõe autoatendimento de exportação ou exclusão de dados pessoais no MVP.

## 7. Incidentes

Suspeita de acesso indevido ou vazamento deve gerar: contenção, preservação de evidências, análise de escopo, registro de decisões e comunicação pelos responsáveis legais quando aplicável. Logs devem ajudar a identificar usuário, Tenant, recurso e momento, sem replicar o dado exposto.

## 8. Critérios antes de produção

- inventário de operadores/subprocessadores aprovado;
- bases legais, canal de privacidade e prazos de retenção formalizados;
- backup e restauração testados;
- revisão de permissões e logs sensíveis;
- procedimento de incidente e de solicitação do titular ensaiados.

## Documentos relacionados

- [Segurança](README.md)
- [Modelo físico do MVP](../architecture/data-model-mvp.md)
- [Regras de negócio](../product/business-rules.md)
- [Auditoria e rastreabilidade](../product/mvp-decisions.md)
