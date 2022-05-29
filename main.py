import os

from database import (commit_projeto_atual, exit_db, icone_atual,
                      insere_pasta_commit, open_db, update_projeto_atual)
from git_utils import get_branch

# ler a pasta atual
pasta_atual = os.getcwd()
print(pasta_atual)


open_db()

pasta_projeto = os.getcwd()
# ler o branch atual
nome_branch_atual = get_branch()
# ler o commit atual do projeto desta pasta no BD
atual = commit_projeto_atual(pasta_projeto)
# ler o icone atual
icone = icone_atual(atual)

exit_db()

# git add
os.system("git add .")
# git commit -m
mensagem_commit = input("Insira a mensagem de commit:\n")
os.system(f'git commit -m "{icone} {mensagem_commit}"')
# checkout main
os.system("git checkout main")
# git rebase com o branch atual
os.system(f"git rebase {nome_branch_atual}")
# git push
os.system("git push")

atual += 1
# git checkout -b <Feat00 numero atual + 1>
os.system(f"git checkout -b Feat{atual+1}")


open_db()
update_projeto_atual(pasta_projeto, atual)

# após fazer o commit incrementar contagem
# criar update para a pasta atual
# salva novo numero de feature na base
# insere_pasta_commit(pasta_projeto, numero_feature)

exit_db()
