from pathlib import Path
import os
from IPython.display import display
os.chdir(Path(__file__).resolve().parent)

# Base fictícia de demonstração; não representa resultados reais.
from IPython.display import display
# Importanto biblioteca
import pandas as pd

# Dataframe da tabela que vou utilzar
df_vendas_geek_store = pd.read_csv("data/vendas_geek_store.csv")

display(df_vendas_geek_store)

# Mostra a tabela com as colunas Produto e Avaliacao Media
display(df_vendas_geek_store[['Produto','Avaliacao_Media']])

# Calcula a receita mostrando as colunas Produto e Receita
df_vendas_geek_store['Receita'] = df_vendas_geek_store['Quantidade_Vendida'] * df_vendas_geek_store['Preco_Venda']
display(df_vendas_geek_store[['Produto','Receita']])

# Calcula o lucro por Unidade e mostra as colunas Produto e Lucro por Unidade
df_vendas_geek_store['Lucro por Unidade'] = df_vendas_geek_store['Preco_Venda'] - df_vendas_geek_store['Custo_Fabricante']
display(df_vendas_geek_store[['Produto','Lucro por Unidade']])

# Calcula o Lucro final mostrando as colunas Produto e Lucro Final
df_vendas_geek_store['Lucro Final'] = df_vendas_geek_store['Lucro por Unidade'] * df_vendas_geek_store['Quantidade_Vendida']
display(df_vendas_geek_store[['Produto','Lucro Final']])

# Cria uma variavel que filtra na coluna Categoria o que estão com Hardware e Periferico
df_filtrado = df_vendas_geek_store[df_vendas_geek_store['Categoria'].isin(['Hardware', 'Periferico', 'Periférico'])]
display(df_filtrado)

df_filtrado.to_csv('vendas_geek_store_filtrada.csv', index=False)
