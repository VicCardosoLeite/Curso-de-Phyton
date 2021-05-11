from time import sleep
print('-=-'*20)
print('Analisador de triângulos!') 
print('-=-'*20)
print('')
sleep(1)
c1 = float(input('Coloque o primeiro segmento: '))
c2 = float(input('Coloque o segundo segmento: '))
c3 = float(input('Coloque o terceiro segmento: '))
print('')
print('Analizando...')
sleep(3)
print('')
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c2 + c1:
    print('Os segmentos acima podem formar um triângulo!')
    