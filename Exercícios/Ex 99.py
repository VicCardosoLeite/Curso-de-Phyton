from time import sleep
def maior(*números):
    cont = maior = 0
    print('\nAnalizando...')
    for valor in números:
        print(f'{valor} ',end='',flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1 
    print(f'Foram informados {cont} valores ao todo!')
    print(f'O maior valor foi {maior}!')


maior(4,6,9,7,10)
maior(4,8,6,3,1,7)
maior(1,8)
maior(9)
maior()
