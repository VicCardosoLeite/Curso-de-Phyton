from Biblioteca.Menu import menu,cabeçalho,leianúmint
from Biblioteca.Funções import arquivoExiste, criaarquivo,lerarquivo,cadastrar
from time import sleep

arquivo = 'cadastro.txt'
if not arquivoExiste(arquivo) == True:
    criaarquivo(arquivo)
while True:
    resposta = menu(['Cadastrar pessoas','Lista de pessoas','Sair do sistema'])
    if resposta == 1:
        sleep(1)
        print()
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leianúmint('Idade: ')
        cadastrar(arquivo,nome,idade)
        
    elif resposta == 2:
        sleep(1)
        print()
        lerarquivo(arquivo)
      
    elif resposta == 3:
        sleep(1)
        print()
        print('Finalizando o sistesma...até logo')
        sleep(3)
        break
    else:
        sleep(1)
        print()
        print('Opção inválida!Tente novamente')
        sleep(2)
