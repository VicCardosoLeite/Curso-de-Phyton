n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
select = 0
while select != 5:
    print('''    (1) Somar
    (2) Multiplicar
    (3) Maior
    (4) Novos números 
    (5) Sair do programa''')
    select = int(input('Qual a opção? R: '))
    if select == 1:
        s = n1 + n2
        print(' {} + {} = {}'.format(n1,n2,s))
    if select == 2:
        p = n1 * n2
        print('{} x {} = {}'.format(n1,n2,p))
    if select == 3:
        if n1 > n2:
            m = n1
        else:
            m = n2
        print('O maior entre {} e {} é {}.'.format(n1,n2,m))
    if select == 4:
        print('Informe os valores novamente: ')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro valor: '))
    if select == 5:
        print('Finalizando...')
print('Fim do programa, volte sempre!')
