from Biblioteca.Menu import menu
from time import sleep
while True:
    resposta = menu(['Cadastrar pessoas','Lista de pessoas','Sair do sistema'])
    if resposta == 1:
        sleep(1)
        print()
        print('1')
    elif resposta == 2:
        sleep(1)
        print()
        print('2')
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
