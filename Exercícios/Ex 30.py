from time import sleep
n = int(input('Digite um número: '))
r = n % 2
print('Processando...')
sleep(3)
if r == 0:
    print('Ele é par')
else:
    print('Ele é ímpar')
