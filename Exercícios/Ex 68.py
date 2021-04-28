from random import randint
print('-=-'*20)
print('Vamos jogar par ou ímpar?')
print('-=-'*20)
cont = 0
while True:
    jogador = int(input('Digite um valor: '))
    compu = randint(0,10)
    tot = jogador + compu
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Quer par ou ímpar?(P/I): ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador jogou {compu}. Dando um total de {tot}')
    if tipo == 'P':
        if tot % 2 == 0:
            print('Você venceu!!!')
            cont += 1
        else:
            print('Você perdeu!!!')
            break
    elif tipo == 'I':
        if tot % 2 == 1:
            print('Você venceu!!!')
            cont += 1
        else:
            print('Você perdeu!!!')
            break
    print('Vamos jogar de novo!')
print(f'Você venceu {cont} vezes.')
