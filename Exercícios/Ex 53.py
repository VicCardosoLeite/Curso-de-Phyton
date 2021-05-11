f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
i = ''
for l in range(len(j) - 1, - 1,- 1):
    i += j[l]
print('A frase digitada foi {} e seu inverso é {}.'.format(j,i))
if i == j:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')
