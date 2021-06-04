from Funções import organiza
from Validador import dinheiro
from time import sleep
valor = dinheiro('Digite um preço: R$')
print()
print('Analizando...')
print()
sleep(3)
organiza(valor)