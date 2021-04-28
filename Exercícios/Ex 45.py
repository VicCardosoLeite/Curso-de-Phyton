from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
pc = randint(0,2)
player = int(input('''Qual você escolhe:
 (0) Digite 0 para escolher Pedra
 (1) Digite 1 para escolher Papel
 (2) Digite 2 para escolher Tesoura
 Jogada: '''))
print('')
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA!!!')
print('-=-'*11)
print('Computador jogou {}.'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[player]))
print('-=-'*11)
if pc == 0: #PC jogou Pedra
    if player == 0:
        print('DEU EMPATE')
    elif player == 1:
        print('JOGADOR VENCE')
    elif player == 2:
        print('COMPUTADOR VENCE')
elif pc == 1: #PC JOGOU PAPEL
    if player == 0: # JOGADOR JOGOU PEDRA
        print('COMPUTADOR VENCE')
    elif player == 1: # JOGADOR JOGOU PAPEL
        print('EMPATE')
    elif player == 2: # JOGADOR JOGOU TESOURA
        print('JOGADOR VENCE')
elif pc == 2: #PC JOGOU Tesoura
    if player == 0: # JOGADOR JOGOU PEDRA
        print('JOGADOR VENCE')
    if player == 1: # JOGADOR JOGOU PAPEL
        print('COMPUTADOR VENCE')
    if player == 2: # JOGADOR JOGOU TESOURA
        print('EMPATE')
