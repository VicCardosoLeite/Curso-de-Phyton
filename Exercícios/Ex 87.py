#Aprimore o desafio anterior mostrando no final:
#a) A soma dos valores pares.
#b) A soma dos valores da terceira coluna
#c) O maior valor da segunda coluna
matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma_par = maior = soma_coluna3 = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a [{l,c}]: '))
print('-=-'*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        #Letra a):
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
    print()
print('-=-'*20)
print(f'A soma dos valores pares é {soma_par}!')
#Letra b):
for l in range(0,3):
    soma_coluna3 += matriz[l][2]
print(f'A soma dos valores da 3ª coluna é {soma_coluna3}')
#Letra c):
for c in range(0,3):
    if c == 0: 
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da 2ª linha é {maior}')
