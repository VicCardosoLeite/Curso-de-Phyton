#Aula 17: Listas(parte 1)
#Para utilizar listas usa: []
#Para adicionar algo na lista usa: 
# lista.append('o que eu quero adicionar'), porem adiciona ao final
#Para adicionar algo sem ser no final usa: 
# lista.insert(posição,o que eu quero adicionar)
#Para deletar algo da lista usa: 
# del lista[indice]/lista.pop(indice)/lista.remove('o que eu quero tirar')
num = [2,5,9,1]
#Substituindo elementos
num[2] = 3
#Adicionando elementos
num.append(7)
#Colocando valores em qualquer posição
num.insert(2,0)
#Colocando em ordem:
num.sort()
print(num)
#Lendo valores no teclado e adicionando em listas:
print('-=-'*20)
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um número: ')))
for c,v in enumerate(valores):
    print(f'Na {c+1}º posição encontrei o valor {v}!')
print('Terminei!!!')
#Fazendo cópia de lista:
print('-=-'*20)
a = [2,4,6,5]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
