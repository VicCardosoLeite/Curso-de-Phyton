#interronpendo o while:
#cont = 1
#while cont <= 10:
    #print(cont)
    #cont += 1
#while True:
    #cont += 1
    #print(cont)
núm = soma = cont = 0
while True:
    núm = int(input('Digite um número: '))
    if núm == 999:
        break
    soma += núm
    cont += 1
print(f'A soma dos {cont} valores é {soma}')