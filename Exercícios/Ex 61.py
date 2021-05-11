from time import sleep
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
print('Gerando PA...')
sleep(3)
t = p
c = 1
tot = 0
more = 10
while more != 0:
    tot = tot + more
    while c <= tot:
            print('{} -> '.format(t),end='')
            t += r
            c += 1
    print('Pausa!')
    more = int(input('Quantos termos a mais você quer mostrar: '))
print('')
print('Você solicitou {} termos.'.format(tot))
print('Fim!')
