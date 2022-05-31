# Faz commit com um comentário prefixado com emoji sequencial
## Branch's sequenciais são criadas, sequência armazenada em Sqlite3

<br>
  <div align="center">
    <table>
      </tr>
            <td>
                <a  href="https://www.linkedin.com/in/robinsonbrz/">
                Idéia e deploy por Robinson Enedino
            </td>
        <td>
            <a  href="https://www.linkedin.com/in/robinsonbrz/">
            <img src="https://raw.githubusercontent.com/robinsonbrz/robinsonbrz/main/static/img/linkedin.png" width="30" height="30">
        </td>
        <td>
            <a  href="https://www.linkedin.com/in/robinsonbrz/">
            <img  src="https://avatars.githubusercontent.com/u/18150643?s=96&amp;v=4" alt="@robinsonbrz" width="30" height="30">
        </td>
        <td>
            <a href="mailto:robinsonbrz@gmail.com">
            <img src="https://raw.githubusercontent.com/robinsonbrz/robinsonbrz/main/static/img/gmail.png" width="30" height="30" ></a>
        </td>
      </tr>
    </table>
  </div>

Visite meu WebSite [https://www.enedino.com.br](https://www.enedino.com.br)
  <br><br><br>

Automatizando o processo de Commit, rebase e push

Criando uma nova branch com numeração sequêncial a cada commit

Faz commit e rebase em main

Após push cria novo branch com um nome sequencial que fica armazenado no sqlite3

Ex: feat001, Feat002 ...

Todo projeto está armazenado em uma pasta no computador,

o caminho da pasta é a chave primária da base, e é armazenada na base de dados com o número do  commit
<br><br>
## Objetivo:

Criar um programa em Python e um executável Windows

que ao ser executado em linha do comando DOS ou PowerShel,

verifica se o projeto já foi armazenado na base de dados, e possui numero de commit

Caso não tenha sido registrado na base, executa esse registro e armazena o número de commit

O programa precisa ser executado na pasta raiz do projeto do Commit

O programa pergunta qual a mensagem de commit, e em seguida efetua o push para o repositório configurado
<br><br>
## Utilização do programa 

Depois de criar o executável pyinstaller.

Copiar o executável rob_reb.exe, gerado na pasta Dist para a pasta C:\dist\

Caso deseje mudar a pasta altere o código de database.py mudando a pasta "connection = sqlite3.connect("c:\dist\projetos_e_commits.db")"

É necessário apontar o diretório "c:\dist\" em variáveis do ambiente no windows
<br><br>
## Após essas configurações, para efetuar um (commit, rebase e push) do seu projeto.

Dentro da pasta do seu projeto execute:

rob_reb.exe

Em prompt você será perguntado qual o commit atual caso seja a primeira utilização nesta pasta de projeto

e também qual a mensagem do commit deseja utilizar

um commit -m, um rebase e um push serão disparados em seguida

Um novo branch será criado "Feat1" para o primeiro e sempre com um número sequencial a partir dos próximos commit.

Ex: Feat2, Feat3...

_______________________


<br>
<br>



<h1 align="center"> Informações e contato </h1> 
  <div align="center">
    <table>
        </tr>
            <td>
                <a  href="https://www.linkedin.com/in/robinsonbrz/">
                <img src="https://raw.githubusercontent.com/robinsonbrz/robinsonbrz/main/static/img/linkedin.png" width="50" height="50">
            </td>
            <td>
                <a  href="https://www.linkedin.com/in/robinsonbrz/">
                <img  src="https://avatars.githubusercontent.com/u/18150643?s=96&amp;v=4" alt="@robinsonbrz" width="30" height="30">
            </td>
            <td>
                <a href="https://www.enedino.com.br/contato">
                <img src="https://raw.githubusercontent.com/robinsonbrz/robinsonbrz/main/static/img/gmail.png" width="50" height="50">
            </td>
        </tr>
    </table> 
  </div>