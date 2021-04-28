#Crie um programa que leia o nome e a nota de vários alunos e no 
#final mostre o boletim e permita que o usuário mostre as notas
#individuais de cada aluno.
from time import sleep
ficha = list()
while True:
    nome = str(input('Digite o nome do aluno(a): '))
    nota1 = float(input('Digite a 1ª nota do aluno(a): '))
    nota2 = float(input('Digite a 2ª nota do aluno(a): '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1,nota2], media])
    resp = str(input('Deseja cadastrar mais um(a) aluno(a)?[S/N] R: '))
    if resp in 'Nn':
        break
    print('-=-'*30)
print('-=-'*20)
print('Gerando boletim...')
sleep(3)
print('-=-'*30)
print(f'{"No.":<4}{"NOME":<15}{"MÉDIA":>3}')
print('-=-'*30)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>3.1f}')
while True:
    print('-=-'*30)
    select = int(input('Mostrar notas de qual aluno?(999 interrompe) R: '))
    if select == 999:
        print('-=-'*30)
        print('Fim do programa, volte sempre!')
        break
    if select <= len(ficha) - 1:
        print(f'Notas de {ficha[select][0]} são {ficha[select][1]}.')
