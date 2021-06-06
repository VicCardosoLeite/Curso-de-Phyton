def leianúmint(mensagem):
    while True:
        try:
            núm = int(input(mensagem))
        except(ValueError, TypeError):
            print('\033[31mDigite um valor inteiro válido!!\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário!')
            return 0
            break
        else:
            return núm


def linhas(tamanho=42):
    return '-'*42


def cabeçalho(texto):
    print(linhas())
    print(texto.center(42))
    print(linhas())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[33m{cont}\033[m - \033[34m{item}\033[m')
        cont += 1
    print(linhas())
    opção = leianúmint('O que deseja fazer? R: ')
    return opção
