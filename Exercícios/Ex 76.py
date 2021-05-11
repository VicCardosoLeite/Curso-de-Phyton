#Crie um programa que tenha uma tupla única com nome de produtos e seus preços,
#na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
lista = ('Borracha', 0.50,
         'Caderno', 30.00,
         'Fichário', 85.90,
         'Mochila', 95.80,
         'Refil de fichário',16.50,
         'Lapiseira(0,7)',12.5,
         'Livro: O Hobbit',45.80)
for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', end='')
    else:
        print(f'R${lista[item]:>5.2f}')