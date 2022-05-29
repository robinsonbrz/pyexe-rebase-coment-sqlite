import sqlite3
import sys

connection = sqlite3.connect("projetos_e_commits.db")
cursor = connection.cursor()


def open_db():
    try:
        cursor.execute("CREATE TABLE posicao_commit ( pasta_projeto STRING, numero_feature INTEGER)")
        cursor.execute("CREATE TABLE icones (numero_icone INTEGER, icone STRING)")
        print("Banco de dados criado com sucesso")
    except Exception as e:
        print("Banco de dados já existe. \nPronto!")
    return


def icone_atual(numero_icone):
    rows = cursor.execute(f"SELECT icone FROM icones Where numero_icone = {numero_icone}").fetchall()
    return rows[0][0]


def commit_projeto_atual(pasta_projeto):
    try:
        str_query = f'SELECT numero_feature FROM posicao_commit Where pasta_projeto = "{pasta_projeto}";'
        rows = cursor.execute(str_query).fetchall()
        retorno = rows[0][0]
        if len(rows) == 0:      # caso não tenha nenhum valor é um projeto novo. insere e retorna 1
            insere_pasta_commit(pasta_projeto, 1)
            retorno  = 1
    except Exception as e:
        print("Erro na busca de commit")
        
    return retorno


def insere_pasta_commit(pasta_projeto, numero_feature):
    str_query = f'INSERT INTO posicao_commit ("pasta_projeto","numero_feature") VALUES ("{pasta_projeto}",{numero_feature});'
    cursor.execute(str_query)
    cursor.execute("commit;")
    return


def exit_db():
    cursor.close()
    connection.close()
    sys.exit()
    return
