# ADR-0002 · Conteúdo privado no MVP
- Estado: adotado na implementação integrada à main em 01/11/2026.
- Contexto: arquivos de até 10 MB e exportações precisam de consistência com metadados, auditoria e isolamento sem depender de provedor já contratado.
- Decisão: a primeira entrega mantém o conteúdo criptografado no MySQL. AES-256-GCM usa chave externa de 32 bytes, nonce aleatório e contexto autenticado com Tenant/ID/proprietário.
- Upload exige MIME/extensão coerentes, validação estrutural e resposta limpa do antimalware ClamAV. Sem scanner ou chave, o serviço não aceita o upload.
- PDFs com conteúdo ativo/embutido são recusados. Downloads são anexos, sem cache e com autorização revalidada.
- A remoção de arquivo é lógica; exportações expiram em 24 h. A política de retenção de anexos continua sujeita à definição anterior a produção.
- Consequências: backups do banco crescem; a chave deve ter backup separado. Perder a chave torna os objetos ilegíveis. A imagem e o banco precisam ter limites de memória/tamanho apropriados.
- Evolução: object storage privado pode substituir a persistência de bytes sem mudar a autorização. Essa migração requer novo ADR, cópia validada e estratégia de rollback.
- Esta decisão não habilita produção nem define provedor ou orçamento.

