import os


def get_branch():
    comando = "git rev-parse --abbrev-ref HEAD"
    os.system(comando + " > tmp")
    retorno = open('tmp', 'r').read()
    os.remove('tmp')
    return retorno
