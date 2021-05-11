from time import sleep
nome = str(input('Qual o seu nome completo?  ')).strip()
sleep(1)
print('Analisando seu nome...')
sleep(3)
a = nome.upper()
b = nome.lower()
c = len(nome) - nome.count(' ')
d=nome.split()
print('Seu nome em maiúsculas é {}'.format(a))
print('Seu nome em minúsculas é {}'.format(b))
print('Seu nome tem {} letras'.format(c))
print('Seu primeiro nome é {} e ele tem {} letras'.format(d[0], len(d[0])))




