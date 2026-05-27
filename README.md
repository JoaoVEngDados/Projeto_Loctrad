# Pipeline de Dados - Mercado Local 🚀

Este repositório contém a infraestrutura de engenharia de dados de *Mercados Locais*, um aplicativo desenvolvido para conectar comerciantes locais aos clientes da região. 

O objetivo central do projeto é descobrir oportunidades reais no mercado local, respondendo perguntas estratégicas de negócio, como: *"Quais bairros têm muita busca por delivery, mas quase nenhum restaurante cadastrado?"*

## Arquitetura e Fluxo (Atualização Semanal)

- **PostgreSQL (Chave-Valor com JSONB):** Gerencia as categorias e tags dos comércios para consultas rápidas.
- **MongoDB (Orientado a Documentos):** Armazena os perfis completos dos lojistas, como horários e avaliações.
- **Python (ETL):** Utiliza **Pandas** e **Numpy** para cruzar informações, limpar os dados e estruturar a base analítica. O pipeline roda de forma automatizada uma vez por semana.
- **Dashboard (Streamlit & Matplotlib):** Camada de visualização final para acompanhar as métricas em gráficos interativos.

## Acompanhamento do Projeto

O detalhamento técnico e a evolução da arquitetura estão documentados na pasta `Detalhes_Projeto_mercado/`. Cada arquivo reflete os logs de desenvolvimento diário, testes de conectividade e blocos de código implementados.
