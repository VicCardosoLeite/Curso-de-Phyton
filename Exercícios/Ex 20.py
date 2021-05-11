from random import shuffle
p1=str(input('Digite o nome do 1 aluno: '))
p2=str(input('Digite o nome do 2 aluno: '))
p3=str(input('Digite o nome do 3 aluno: '))
p4=str(input('Digite o nome do 4 aluno: '))
alunos=[p1,p2,p3,p4]
shuffle(alunos)
print('A ordem será: ')
print(alunos)
