

import pyodbc
import pandas as pd

dados_conexao = (
    "Driver={SQL Server};"
    "Server=HDLS0101;"
    "Database=Cliente360"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

comando_sql="SELECT * FROM TbProdutos"

dados=pd.read_sql(comando_sql, conexao)

display(dados)
