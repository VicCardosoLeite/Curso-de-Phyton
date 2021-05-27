#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado. No final serão exibidos todos os valo-
#-res únicos digitados, em ordem crescente.

#Fazendo a lista
número = list() 
while True:
    valor = int(input('Digite um valor: '))
    if valor not in número: #Verificando se o valor já tá na lista
        número.append(valor) #Adicionado os valores do usuário a lista 
        print('Valor adicionado com sucesso!')
    else:
        print('Valor existente não irei adicionar!')
    select = str(input('Deseja continuar?[S/N] R: ')).strip() #Perguntando ao usuário
    if select in 'Nn': #Quebrando o looping
        break
print('-=-'*20)
número.sort() #Ordenando a lista
print(f'Os valores informados foram:{número}')
