galera = list()
pessoas = dict()
soma = media = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo(M/F): ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F por favor.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Deseja cadastrar mais uma pessoa?[S/N] R: ')).upper()[0]
        print('-=-'*20)
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N por favor.')
    if resp == 'N':
        break
media = soma / len(galera)
print('-=-'*20)
print(f'Ao todos foram cadastradas {len(galera)} pessoas!')
print(f'A média das idades é {media:5.2f} anos!')
print(f'As mulheres cadastradas foram ',end=' ')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=',')
print()
print('Esses estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ',end='')
        for k,v in p.items():
            print(f'{k} = {v}; ',end='')
print('Fim do programa!')
