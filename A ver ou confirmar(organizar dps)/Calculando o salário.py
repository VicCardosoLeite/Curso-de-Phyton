from time import sleep
d=float(input('Quanto você ganha por hora? R: '))
h=float(input('Quantas horas por mês vc trabalha? R: '))
s=d*h
print('Calculando...')
sleep(3)
print('Seu salário mensal é R${}.'.format(s))
