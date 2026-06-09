# 🚀 Relatório Diário de Projeto Loctra - Dia 02 _ Ingestao de dados

## 📌 Objetivo do Dia
Criação do script de ingestão de dados para consumir dados brutos de comércios locais e distribuí-los de forma híbrida entre bancos SQL e NoSQL.

## 🛠️ Atividades Realizadas
- **Simulação de API:** Estruturação de payload JSON simulando o retorno de serviços de geolocalização de comércios.
- **Carga PostgreSQL (Chave-Valor):** Implementação de lógica de `UPSERT` para persistir categorias (chave) e tags associadas (valor em `JSONB`).
- **Carga MongoDB (Documentos):** Persistência do documento completo e aninhado de cada lojista utilizando a operação `update_one` com `upsert=True` para evitar duplicidade.

## 🧪 Cobertura de Testes e Validação
- [x] Script executado sem quebras de encoding.
- [x] Verificação no PostgreSQL: Registros inseridos corretamente na tabela `categorias_kv`.
- [x] Verificação no MongoDB: Coleção `lojas_detalhes` populada com estruturas de subdocumentos intactas.

## 💻 Blocos de Código-Chave
*Lógica de distribuição dos dados no Python:*
\`\`\`python
# Carga em formato Chave-Valor (Postgres)
pg_cursor.execute("""
    INSERT INTO categorias_kv (chave, valor) VALUES (%s, %s)
    ON CONFLICT (chave) DO UPDATE SET valor = EXCLUDED.valor;
""", (chave, valor_json))

# Carga em formato Documento (MongoDB)
mongo_col.update_one({"id_loja": loja["id_loja"]}, {"$set": loja}, upsert=True)
\`\`\`