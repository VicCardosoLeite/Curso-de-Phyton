from time import sleep
cont = 0
méd = soma = quant = 0
unid = 0
print('-=-'*20)
print('                Calculador de média                    ')
print('-=-'*20)
print('')
print('Carregando...')
sleep(3)
print('-'*30)
unid = int(input('Quantas unidades? R: '))
print('-'*30)
while unid < cont:
    cont += 1
    nota = float(input('Digite sua {} nota: '.format(cont)))
    soma += nota
    if cont > unid:
        break
méd = soma / unid
print('Calculando...')
print('-'*30)
sleep(3)
print('Sua média é {:.1f}!'.format(méd))
if 5 <= méd < 6:
    print('Cuidado estude mais!')
elif 7 <= méd < 8:
    print('Parabéns você está na média!!')
elif 8 <= méd <= 10:
    print('Meus parabéns você está com uma ótima média, continue assim!')
print('')
print('Fim do programa')
