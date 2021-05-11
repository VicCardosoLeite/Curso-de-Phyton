pessoa18 = homem = mulheres20 = cont = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo(M/F): ')).strip().upper()[0]
    if idade > 18:
        pessoa18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?(S/N): ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Pessoas com mais de 18 anos: {pessoa18}')
print(f'Mulheres com mais de 20 anos: {mulheres20}')
print(f'Quantidade de homens cadastrados: {homem}')