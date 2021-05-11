#Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já
#posição correta(sem usar sort()). No final mostre a lista ordenada na tela.
valores = list()
for c in range(0,5):
    núm = int(input('Digite um valor: '))
    if c == 0 or núm > valores[-1]:
        valores.append(núm)
        print('Adicionado ao final da lista!')
    else:
        pos = 0
        while pos < len(valores):
            if núm <= valores[pos]:
                valores.insert(pos, núm)
                print(f'Adicionado na posição {pos} da lista!')
                break
            pos += 1
print('-=-'*20)
print(f'Os valores digitados em ordem foram: {valores}')
