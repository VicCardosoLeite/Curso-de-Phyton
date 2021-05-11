from random import randint
from time import sleep
def sorteia(lista):
    for cont in range(0,5):
        mostra = randint(1,10)
        lista.append(mostra)
        print(f'{mostra} ',end='',flush=True)
        sleep(0.4)
    print('Acabei')

def par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares é {soma}')
núm = list()
sorteia(núm)
par(núm)
