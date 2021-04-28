aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['média'] = float(input(f'Qual a média de {aluno["nome"]}: '))
if aluno['média'] < 7:
    print(f'Infelizmente {aluno["nome"]} está reprovado(a)! Estude mais')
if aluno['média'] >= 7:
    print(f'Parabéns {aluno["nome"]} você passou de ano! Boas férias!')
