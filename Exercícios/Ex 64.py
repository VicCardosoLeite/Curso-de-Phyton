número = cont = soma = 0
while n != 999:
    número = int(input('Digite um número(digite 999 para parar): '))
    cont += 1
    soma += número
    d = soma - 999
print(f'Você digitou {cont} termos e a soma entre eles é {soma}!')
