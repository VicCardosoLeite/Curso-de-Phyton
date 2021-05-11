valores = list()
par = list()
impar = list()
while True:
    valores.append(int(input('Digite um número: ')))
    select = str(input('Deseja continuar?[S/N] R: ')).strip().upper()
    if select in 'N':
        break
for i,v in enumerate(valores):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('-=-'*20)
print(f'A lista completa é : {valores}')
print(f'Os pares são {par}')
print(f'Os ímpares são {impar}')
