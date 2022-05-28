import sqlite3
import sys

connection = sqlite3.connect("projetos_e_commits.db")
cursor = connection.cursor()

try:
    cursor.execute("CREATE TABLE posicao_commit ( pasta_projeto STRING, numero_feature INTEGER)")
    cursor.execute("CREATE TABLE icones (numero_icone INTEGER, icone STRING)")
    print("Banco de dados criado com sucesso")
except Exception as e:
    print("Banco de dados já existe. \nPronto!")



def retorna_icone(numero_icone):
    rows = cursor.execute(f"SELECT icone FROM icones Where numero_icone = {numero_icone}").fetchall()
    return rows[0][0]



print(retorna_icone(1))
