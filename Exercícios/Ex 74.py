from random import randint
from time import sleep
print('Carregando...')
sleep(5)
num = (randint(1, 10) , randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram: {num}')
print('-=-'*10)
print(f'O maior valor foi: {max(num)}')
print('-=-'*10)
print(f'O menor valor foi: {min(num)}')
print('-=-'*10)
print(f'Fim do programa, muito obrigado por ter utilizado!')
