def leianúm(mensagem):
    Ok = False
    Valor = 0
    while True:
        núm = str(input(mensagem))
        if núm.isnumeric():
            Valor = int(núm)
            Ok = True
        else:
            print('ERRO!!Digite um número inteiro válido(Ex: 5,4,3,...)')
        if Ok:
            break
    return Valor
    

número = leianúm('Digite um número: ')
print(f'Você digitou o número {número}')
