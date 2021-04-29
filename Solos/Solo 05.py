nome = str(input('Qual o seu nome completo? R: ')).strip()
data = str(input('Digite seu ano de nascimento(Ex:dd mm aaaa(a=ano,d=dia,m=mês): '))
u = nome.upper()
a = u.count('A')
b = nome.split()
c = b[len(b)-1]
d = data.split()
e = d[len(d)-1]
f = int(e)
h = 2021 - f
print('Prazer em te conhecer {}!'.format(nome[0:3]))
print('Analizando seu os dados...')
print('')
print('Seu nome tem {} letras a.'.format(a))
print('Seu primeiro nome é {}.'.format(b[0]))
print('Seu último nome é {}.'.format(c))
print('E você tem {} anos.'.format(h))