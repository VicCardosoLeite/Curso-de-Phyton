import random
al1=str(input('Digite o nome do primeiro aluno: '))
al2=str(input('Digite mais um nome: '))
al3=str(input('Digite outro: '))
al4=str(input('Digite o último nome: '))
sorteio = [al1,al2,al3,al4]
escolhido = random.choice(sorteio)
print('O escolhido(a) foi {}.'.format(escolhido))
