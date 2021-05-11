#Listas parte 2:
#Como adicionar listas dentro de listas:
#lista1.append(lista2[:])
#lista1 = [['objeto1,objeto2'],['objeto3','objeto4']]
#Para acessar itens específicos:
#print(lista[indice(lista)][indice(objeto que eu quero ver)])
teste1 = list()
teste1.append('Guto')
teste1.append(25)
teste2 = list()
teste2.append(teste1[:]) 
teste1[0] = 'Marta'
teste1[1] = 28
teste2.append(teste1[:])
print(teste1)
print('-=-'*20)
print(teste2)
print('-=-'*20)
teste3 = [['Vitor',18], ['Ana',15], ['Beatriz',17], ['João',7]] #Declarando lista
print(teste3)
#Isolando um indice da lista:
print('-=-'*20)
print(teste3[0][0])
print('-=-'*20)
for p in teste3:
    print(f'{p[0]} tem {p[1]} anos de idade!') 
#Pode ser útil:
print('-=-'*20)
teste4 = list() #lista principal
dados = list() #lista secundária
for c in range(0,3):
    dados.append(str(input('Digite o nome da pessoa: ')))
    dados.append(int(input('Digite a idade da pessoa: ')))
    teste4.append(dados[:]) #Adicionando uma cópia da lista dados na lista principal
    dados.clear()
print(teste4)
