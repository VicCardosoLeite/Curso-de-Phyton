#Serve para quando não souber o limite.
#Em português esse comando significa enquanto.
n = 1
R = 'S'
par = imp = 0
while R == 'S':
    n = int(input('Digite um valor: '))
    R = str(input('Quer continuar(S/N): ')).upper()
    if n % 2 == 0:
        par += 1
    else:
        imp += 1
print('''Pares: {}
Ímpares: {}'''.format(par,imp))
print('FIM')
