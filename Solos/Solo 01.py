from time import sleep
print('Olá,sou Uni e vou ser sua ajudante no mundo da soma')
print('(Para para digite 0)')
n = 1
s = 0
while n != 0:
    n = int(input('Informe o valor: '))
    s += n
print('Calculando...')
sleep(3)
print('O total(soma) é {}'.format(s))
print('Espero ter ajudado, te vejo depois')
