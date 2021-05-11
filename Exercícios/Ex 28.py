from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5! Tente adivinhar!')
print('-=-'*20)
computador = randint(0,5)
jogador = int(input('Qual a sua jogada? R: '))
print('')
print('Processando...')
sleep(3)
print('')
if computador == jogador:
    print('Parabéns você ganhou!')
else:
    print(f'Hahaha ganhei! O número sorteado foi {computador}')
