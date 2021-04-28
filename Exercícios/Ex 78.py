#Faça um programa que leia 5 valores e uarde-os em uma lista. No final mostre o maior e menor
#valor digitado e suas posições.
#Criando a lista e contadores:
valores = list()
maior = 0
menor = 0
for cont in range (0,5): #Colocando os valores dentro da lista
    valores.append(int(input(f'Digite o valor para a {cont}: ')))
    #Verificando o maior e o menor
    if cont == 0: 
        maior = menor = valores[cont] #Pra se o maior for o primeiro número digitado
    else: #Se for outro valor
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f'Os valores digitados foram: {valores}')
print(f'O maior valor foi: {maior} nas posições ',end='')
for i , v in enumerate(valores): #Vendo a posição do maior valor
    if v == maior:
        print(f'{i}..',end='')
print(f'\nO menor foi {menor} nas posições ',end='') #Vendo a posição do menor valor
for i,v in enumerate(valores):
    if v == menor:
        print(f'{i}..',end='')
