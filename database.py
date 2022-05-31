import sqlite3
import sys

# cria banco na pasta c:\dist
# ou conecta em base já criada anteriormente
connection = sqlite3.connect("c:\dist\projetos_e_commits.db")
cursor = connection.cursor()


def open_db():
    try:
        cursor.execute("CREATE TABLE posicao_commit ( pasta_projeto STRING, numero_feature INTEGER)")
        cursor.execute("CREATE TABLE icones (numero_icone INTEGER, icone STRING)")
        print("\n")
    except Exception as e:
        print("\n")
    return


def icone_atual(numero_icone):
    str_sql = f"SELECT icone FROM icones Where numero_icone = {numero_icone}"
    # print(str_sql)
    rows = cursor.execute(str_sql).fetchall()
    return rows[0][0]


def commit_projeto_atual(pasta_projeto):
    try:
        str_query = f'SELECT numero_feature FROM posicao_commit Where pasta_projeto = "{pasta_projeto}";'
        rows = cursor.execute(str_query).fetchall()
        # print(f"retorno {rows}")
        if len(rows) == 0:      # caso não tenha nenhum valor é um projeto novo. insere e retorna 1
            num_commit = input("Ainda não existe nenhum commit registrado,\ninsira o numero atual do commit: \n")
            insere_pasta_commit(pasta_projeto, int(num_commit))
            retorno  = int(num_commit)
        else:
            retorno = rows[0][0]
    except Exception as e:
        print(e)
    return retorno


def update_projeto_atual(pasta_projeto, numero_commit_atual):
    str_query  = f'UPDATE posicao_commit SET numero_feature = {numero_commit_atual} WHERE pasta_projeto = "{pasta_projeto}"' # noqa E501
    try:
        cursor.execute(str_query)
        connection.commit()
        # print('Successo na atualização!')
    except Exception as e:
        print(e)
    return


def insere_pasta_commit(pasta_projeto, numero_feature):
    str_query = f'INSERT INTO posicao_commit ("pasta_projeto","numero_feature") VALUES ("{pasta_projeto}",{numero_feature});'
    cursor.execute(str_query)
    cursor.execute("commit;")
    return


def exit_db():
    try:
        cursor.close()
        connection.close()
    except Exception as e:
        print(e)
    return
