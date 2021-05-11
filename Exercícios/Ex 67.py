n = cont = 0
while True:
    n = int(input('Digite um valor para ver sua tabuada(insira um número negativo para parar): '))
    if n < 0:
        break
    print ( '-' * 30 )
    for cont in range(1,11):
        print(f'{n} x {cont} = {n*cont}')
    print('-'*30)
print('Obrigada, volte sempre!')
