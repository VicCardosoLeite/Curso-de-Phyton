#Faça um programa que faça n jogos da mega sena, cadastrando os números em uma lista:
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-=-'*20)
print(                        'MEGA SENA'                         )
print('-=-'*20)
quant = int(input('Quantos jogos você quer fazer? R: '))
print('')
tot = 1
while tot <= quant:
    cont = 0
    while True:
        número = randint(1,60)
        if número not in lista:
            lista.append(número)
            cont += 1 
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('Carregando...')
sleep(3)
print('-=-'*20)
for i,l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
