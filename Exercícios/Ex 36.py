from time import sleep
casa = float(input('Qual o valor da casa? R$ '))
sac = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? R: '))
pr = casa / (anos * 12)
m = sac * 30 / 100
print('')
print('Calculando a prestação...')
print('')
sleep(3)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação é de R${:.2f}.'.format(casa,anos,pr))
print('')
print('Analizando...')
print('')
sleep(3)
if pr <= m:
    print('Empréstimo concedido! ')
else:
    print('Empréstimo negado!')
