from random import randint
from time import sleep
compu = randint(0,10)
print('-=-'* 20)
print('\033[0;32mVou pensar em um número entre 0 e 10. Tente adivinhar...\033[m')
print('-=-' * 20)
sleep(1)
a = False
jogadas = 0
while not a:
    jogador = int(input('Em que número eu pensei? R: '))
    jogadas += 1
    if jogador == compu:
        a = True
    else:
        if jogador < compu:
            print('Mais...Tente denovo!')
        elif jogador > compu:
            print('Menos...Tente denovo!')
print(f'Acertou com {jogadas} tentativas. Parabéns!!!')
