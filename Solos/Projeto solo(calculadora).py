#Teste
from time import sleep
soma = mult = 0
print('-=-'*20)
print('Bem vindo a calculadora super completa!')
print('-=-'*20)
print('Carregando...')
sleep(3)
print('')
print('Legenda:')
print('a = soma')
print('b = multiplicação')
print('c = divisão')
print('d = geometria plana')
print('e = geometria espacial')
print('f = tabuada')
print('')
select = input('Digite a operação que você deseja fazer. R: ')
print('')
print('Processando...')
sleep(2)
print('')
if select == 'a':
    print('Ok, você selecionou soma!')
    print('')
    quant = int(input('Quantos números você deseja somar: '))
    for c in range(0,quant):
        núm = float(input(f'Digite o {c+1}º número: '))
        soma += núm
    print('Calculando...')
    sleep(3)
    print(f'A soma entre os números digitados é {soma}')
if select == 'b':
    quant = int(input('Quantos números você deseja multiplicar: '))
    for c in range(0,quant):
        núm = float(input(f'Digite o {c+1}º número: '))
        núm 
    print(f'A multiplicação entre os números digitados foi {mult}')