from time import sleep
def cont(início, fim, passo):
     if passo < 0:
        passo *= -1
     if passo == 0:
        passo = 1
     print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    #a)
     if início < fim:
        cont = início
        while cont <= fim:
            print(f'{cont} ',end='',flush=True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    #b)
     else:
        cont = início
        while cont >= fim:
            print(f'{cont} ',end='',flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM!')


cont(1, 10, 1)
print('-=-'*20)
cont(10, 0, 2)
print('-=-'*20)
print('Agora é sua vez!')
print('-=-'*20)
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
cont(ini, fim, pas)
