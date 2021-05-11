#Crie um programa que crie uma matriz 3x3 e a preencha com valores fornecidos pelo usuário
#No final mostre a matriz com a forma correta.
matriz = [[0,0,0], [0,0,0], [0,0,0]] #Matriz
for l in range(0,3): #Linhas
    for c in range(0,3): #Colunas
        matriz[l][c] = int(input(f'Digite um valor para a [{l,c}]: '))
print('-=-'*20)
for l in range(0,3): #Deixando a matriz arrumada 
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='') 
    print()
