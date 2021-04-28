dia=int(input('Quantos dias o carro ficou com vc? '))
km=float(input('Quantos Km vc andou com um carro? '))
pago=(dia * 60) + (km * 0.15)
print('O valor é R${:.2f}'.format(pago))