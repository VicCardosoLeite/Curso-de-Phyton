from time import sleep
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print('')
print('Analizando...')
print('')
sleep(3)
if n1 > n2:
    print('O primeiro número é maior!')
elif n2 > n1:
    print('O segundo valor é maior!')
else:
    print('Os dois são iguais!')
