from time import sleep
d = float(input('Quantos Km de distância tem entre o seu destino e a cidade/estado onde você está? R: '))
if d <= 200:
    p = d*0.50
else:
    p = d * 0.45
print('Calculando o preço...')
sleep(4)
print('Tenha uma boa viagem! A passagem custa R${:.2f}.'.format(p))