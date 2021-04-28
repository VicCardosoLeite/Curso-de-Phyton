from datetime import date
a = date.today().year
tm = 0
tmn = 0
for c in range(1,8):
    nasc = int ( input ( 'Digite o ano de nascimento da pessoa {}: ' ).format(c) )
    i = a - nasc
    if i >= 18:
        tm += 1
    else:
        tmn += 1
print('-*-'*20)
print('Ao todo tivemos {} pessoas maiores de idade.'.format(tm))
print('E {} menores de idade.'.format(tmn))

