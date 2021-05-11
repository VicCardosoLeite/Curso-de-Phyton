from time import sleep
r=float(input('Quantos reais vc tem? R$'))
d= r / 5.55
print('Calculando...')
sleep(3)
print('Com R${:.2f} vc compra US${:.2f}'.format(r,d))
print('')
print('Boa sorte, você está no Brasil.')
