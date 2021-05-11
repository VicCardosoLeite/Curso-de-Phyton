#Crie um programa que leia 7 números e os guarde dentro de uma lista e depois mostre os valores
#pares e ímpares:
valor = [[], []]
núm = 0
for c in range(1,8):
    núm = int(input(f'Digite o {c}º valor: '))
    if núm % 2 == 0:
        valor[0].append(núm)
    else:
        valor[1].append(núm)
valor[0].sort()
valor[1].sort()
print(f'O valores pares foram: {valor[0]}')
print(f'Os valores ímpares foram: {valor[1]}')
