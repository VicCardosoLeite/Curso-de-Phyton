#Faça um programa para fazer cadastro de pessoas, depois forneça:
#a) A idade da pessoa mais velha ok
#b) A idade da pessoa mais nova ok
#c) A soma das idades 
menor = 0
maior = 0
soma = 0
idade = list()
quantidade_de_pessoas = int(input('Quantas pessoas você quer cadastrar: '))
for cont in range(0,quantidade_de_pessoas):
    nome = str(input('Digite o nome da pessoa: ')).strip()
    idade.append(int(input(f'Digite a idade da pessoa: ')))
    soma += idade[cont] #A soma das idades
    print('-=-'*20) 
    if cont == 0:
        maior = menor = idade[cont]
    else:
        if idade[cont] > maior: #Letra a)
            maior = idade[cont]
        elif idade[cont] < menor: #Letra b)
            menor = idade[cont]
print(f'A pessoa mais velha tem {maior} anos.')
print(f'A pessoa mais nova tem {menor} anos.')
print(f'A soma das idades foi: {soma}')
