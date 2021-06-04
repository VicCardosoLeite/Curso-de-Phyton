from time import sleep
salário = float ( input ( 'Quanto você ganhava? R$ ' ) )
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('')
print('Calculando...')
sleep(3)
print('')
print('Seu novo salário é {:.2f}.'.format(novo))
"4"