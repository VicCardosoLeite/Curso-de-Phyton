n = str(input('Digite seu nome completo: ')).strip()
a = n.split()
b = a[len(a)-1]
print('Prazer em te conhecer {}!'.format(n))
print('Seu primeiro nome é {}'.format(a[0]))
print('E seu último nome é {}.'.format(b))





