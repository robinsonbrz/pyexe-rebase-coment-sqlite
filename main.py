import os

from database import (commit_projeto_atual, exit_db, icone_atual,
                      insere_pasta_commit, open_db)

# ler a pasta atual
pasta_atual = os.getcwd()
print(pasta_atual)


open_db()
commit_projeto_atual(pasta_atual)
pasta_projeto = "asdfgh"
numero_feature = 55
print(commit_projeto_atual(pasta_projeto))
insere_pasta_commit(pasta_projeto, numero_feature)
exit_db()





# ler o commit atual do projeto desta pasta

# armazenar o último commit
# armazenar pasta

# ao fazer o commit incrementar contagem
# fazer rebase
# fazer checkout -b # seq feat



