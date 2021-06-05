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
    print('Muito obrigado, volte sempre!')

def leianúmfloat(mensagem):
    while True:
        try:
            núm = float(input(mensagem))
        except(ValueError,TypeError):
            print('\033[31mDigite um número real válido(Exemplos: 9.4,7.4,8.0)\033[m')
            continue
        except(KeyboardInterrupt):
            print('O usuário preferiu interromper o programa!')
            return 0
            break
        else:
            return núm


valor1 = leianúmint('Digite um número inteiro: ')
valor2 = leianúmfloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {valor1} e o real foi {valor2}!')
