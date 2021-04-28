#Crie um programa com uma tupla de várias palavras(não usar acentos). Depois mostre as vogais
#de cada palavra
palavras = ('Cafe','Bolo','Computaçao','Ciencia',
            'Faculdade','Socorro','Sorvete','Sei la')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')
            