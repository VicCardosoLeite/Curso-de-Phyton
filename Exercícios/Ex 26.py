fr = str(input('Digite uma frase: ')).strip().upper()
a = fr.count('A')
b = fr.find('A')+1
c = fr.rfind('A')
print('A letra A aparece {} vezes na frase.'.format(a))
print('A letra A aparece pela primeira vez na posição {}'.format(b))
print('A letra A aparece pela última vez na posição {}.'.format(c))
