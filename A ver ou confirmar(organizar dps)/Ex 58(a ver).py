from random import randint
from time import sleep
compu = randint(0,10)
print('\033[0;35m-=-\033[m'* 20)
print('\033[0;32mVou pensar em um número entre 0 e 10. Tente adivinhar...\033[m')
print('\033[0;35m-=-\033[m' * 20)
sleep(1)
a = False
p = 0
while not a:
    j = int(input('Em que número eu pensei? R: '))
    p += 1
    if j == compu:
        a = True
    else:
        if j < compu:
            print('Mais...Tente denovo!')
        elif j > compu:
            print('Menos...Tente denovo!')
print('Acertou com {} tentativas. Parabéns!!!'.format(p))
