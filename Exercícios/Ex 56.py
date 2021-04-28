si = 0
mi = 0
mih = 0
nv = ''
tm = 0
for p in range(1 , 5):
    print('---- {}ª Pessoa ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    gênero = str(input('Sexo(M/F): ')).strip()
    si += idade
    mi = si / 4
    if p == 1 and gênero in 'Mm':
        mih = idade
        nv = nome
    if gênero in 'Mm' and idade > mih:
        mih = idade
        nv = nome
    if gênero in 'Ff' and idade < 20:
        tm += 1
print('A média das idades é {}'.format(mi))
print('O homem mais velho é {} e tem {} anos.'.format(nv,mih))
print('E {} mulheres tem menos de 20 anos.'.format(tm))