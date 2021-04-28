from math import ceil
from time import sleep
print('Seja bem vindo(a) ao calculador de média, primeiro preciso saber o seu nome')
print('')
nome=input('Nome do aluno(a):')
print('Olá {}, agora me informe suas notas abaixo:'.format(nome))
print('')
n1=float(input('Digite a nota da 1 unidade:'))
n2=float(input('Digite a nota da 2 unidade:'))
media=(n1+n2) / 2
print('Calculando...')
sleep(3)
print('Sua média é {:.1f}'.format(media))
print('')
print('Analizando...')
print('')
sleep(2)
if media < 5:
    print('Sinto muito mas você está reprovado(a)! Estude mais próximo ano!')
elif 6.9 > media >= 5:
    print('Infelizmente você está de recuperação! Estude e tente passar de ano!')
elif media >= 7:
    print('Parabéns você passou! Boas férias!')
