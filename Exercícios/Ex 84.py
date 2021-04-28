#Crie um programa que analise o peso de várias pessoas,guardando em uma lista, e depois mostre o nome 
# e o peso das pessoas mais pesadas e as das mais leves, também mostre a 
# quantidade de pessoas cadastradas:
list_temp = list()
list_principal = list()
maior = menor = cont_fem = 0
while True:
    list_temp.append(str(input('Digite o nome da pessoa: ')))
    list_temp.append(float(input('Digite o peso da pessoa: ')))
    if len(list_principal) == 0:
        maior = menor = list_temp[1]
    else:
        if list_temp[1] > maior:
            maior = list_temp[1]
        elif list_temp[1] < menor:
            menor = list_temp[1]
    list_principal.append(list_temp[:])
    list_temp.clear()
    resp = str(input('Deseja adicionar mais uma pessoa?[S/N] R: ')).strip()
    if resp in 'Nn': 
        break
print('-=-'*20)
print(f'Você cadastrou {len(list_principal)} pessoas!')
print(f'O maior peso foi de {maior}Kg! Peso de ',end=' ')
for p in list_principal:
    if p[1] == maior:
        print(f'[{p[0]}]',end='')
print(f'nO menor peso foi de {menor}Kg! Peso de ',end='')
print()
for p in list_principal:
    print(f'[{p[0]}]', end='')
