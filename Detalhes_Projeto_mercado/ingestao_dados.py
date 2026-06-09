# -*- coding: utf-8 -*-
import io,sys,os,json,psycopg2
from pymongo import MongoClient

# Ajuste de encoding para o terminal
os.environ['PYTHONIOENCODING'] = 'utf-8'
os.environ['PGCLIENTENCODING'] = 'UTF8'

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8',errors='replace')

#Configurações

PG_CONFIG = {"dbname":"loctra_db","user":"postgres","password":"123456789","host":"localhost"}
MONGO_URI = "mongodb://localhost:27017/"

#1 Simulação dos dados que viriam da Api da Internet

dados_api = [{
    
        "id_loja": "LJ001",
        "nome": "Panificadora Alfa",
        "categoria": "padaria",
        "bairro": "Centro",
        "detalhes": {"horario": "06:00-20:00", "nota_media": 4.7, "delivery": True},
        "tags_busca": ["pao", "cafe", "confeitaria"]

},{
    
        "id_loja": "LJ002",
        "nome": "Festa no Hamburguer",
        "categoria": "restaurante",
        "bairro": "Zona Leste",
        "detalhes": {"horario": "18:00-23:30", "nota_media": 4.2, "delivery": True},
        "tags_busca": ["lanche", "burguer", "artesanal"]

},{
        "id_loja": "LJ003",
        "nome": "Drogaria Piauí",
        "categoria": "farmacia",
        "bairro": "Centro",
        "detalhes": {"horario": "24h", "nota_media": 4.5, "delivery": False},
        "tags_busca": ["remedio", "saude", "higiene"]

}]

def executar_ingestao():
    try:
        #Conectando os bancos

        pg_connec = psycopg2.connect(**PG_CONFIG)

        pg_cursor = pg_connec.cursor()

        mongo_client = MongoClient(MONGO_URI)
        mongo_db = mongo_client["loctra_db"]
        mongo_colec = mongo_db["lojas_detalhes"]

        print("🔄 Iniciando ingestão dos dados...")

        for loja in dados_api:
            
            # --- PARTE 1: POSTGRESQL (Chave-Valor) ---
            # Chave: categoria | Valor: tags de busca em formato JSONB
           chave = loja["categoria"]
           valor_json = json.dumps({"tags":loja["tags_busca"]})

           # Upsert (Insere ou atualiza se a chave já existir)
           pg_cursor.execute("""
                INSERT INTO categorias_kv (chave, valor) 
                VALUES (%s, %s)
                ON CONFLICT (chave) DO UPDATE SET valor = EXCLUDED.valor;
            """, (chave, valor_json))
           # --- PARTE 2: MONGODB (Orientado a Documentos) ---
            # Salva o documento completo do comércio
           mongo_colec.update_one(
               {"id_loja":loja["id_loja"]},
               {"$set":loja},
               upsert=True
            )
           
        pg_connec.commit()
        pg_cursor.close()
        pg_connec.close()
        print("✅ Dados ingeridos com sucesso no Postgres e MongoDB!")

    except Exception as e:
        print(f"❌ Erro durante a ingestão: {e}")

if __name__ == "__main__":
    executar_ingestao()   