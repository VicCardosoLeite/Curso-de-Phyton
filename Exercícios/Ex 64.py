n = cont = s = 0
n = int(input('Digite um número(digite 999 para parar): '))
while n != 999:
    cont += 1
    s += n
    d = s - 999
    n = int ( input ( 'Digite um número(digite 999 para parar): ' ) )
print('Você digitou {} termos e a soma entre eles é {}!'.format(cont,s))
