# 🚀 Relatório Diário de Projeto mercado - Dia 01

## 📌 Objetivo do Dia
Configuração do ambiente local de controle de versão, provisionamento das bases de dados e validação de conectividade via Python com tratamento de *encoding*.

## 🛠️ Atividades Realizadas
- **PostgreSQL:** Criação do banco `loctra_db` e da tabela `categorias_kv` estruturada em `JSONB`.
- **MongoDB:** Inicialização do banco `loctra_db` e da coleção `lojas_detalhes`.
- **Python:** Desenvolvimento do script `setup_conexao.py` com suporte a `UTF-8` nativo e tratamento de exceções de decodificação (`UnicodeDecodeError`) para o terminal Windows.

## 🧪 Cobertura de Testes e Validação
- [x] Handshake com PostgreSQL estabelecido com sucesso.
- [x] Comando `ping` executado com sucesso no cluster local do MongoDB.
- [x] Tratamento de caracteres especiais e acentuação validado no terminal.

## 💻 Blocos de Código-Chave
*Script de validação e ajuste de ambiente Python:*
\`\`\`python
# Tratamento de encoding para logs limpos no terminal
os.environ['PYTHONIOENCODING'] = 'utf-8'
os.environ['PGCLIENTENCODING'] = 'UTF8'

try:
    pg_conn = psycopg2.connect(**PG_CONFIG)
    print("✅ PostgreSQL conectado com sucesso!")
except UnicodeDecodeError as e:
    mensagem = e.object.decode('latin-1')
    print(f"❌ Erro PostgreSQL: {mensagem}")
\`\`\`
