from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print ( 'Você tem {} anos'.format ( idade) )
if idade <= 9:
    print ( 'Sua categoria é mirim. Boa sorte!')
elif idade <= 14:
    print ( 'Sua categoria é infantil. Boa sorte!')
elif idade <= 19:
    print ( 'Sua categoria é junior. Boa sorte!')
elif idade <= 25:
    print('Sua categoria é sênior. Boa sorte!')
elif idade > 25:
    print( "Sua categoria é master. Boa sorte!" )




