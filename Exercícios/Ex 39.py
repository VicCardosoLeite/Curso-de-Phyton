from time import sleep
from datetime import date
g = str(input('Você é homem ou mulher? R: ').strip()).upper()
if g == 'HOMEM':
    ano = int(input('Informe o seu ano de nascimento: '))
    atual = date.today().year
    idade = atual - ano
    print('')
    print('Analizando...')
    print('')
    sleep(3)
    print('Você tem {} anos em {}.'.format(idade,atual))
    if idade == 18:
        print('Você já é obrigado a se alistar! Não perca tempo!')
    elif idade < 18:
        s = 18 - idade
        a = atual + s
        print('Você ainda não tem 18 anos, faltam {} anos para você se alistar.'.format(s))
        print('Seu alistamento será em {}.Não se esqueça!'.format(a))
    elif idade > 18:
        s = idade - 18
        a = atual - s
        print('Você deveria ter alistado há {} anos.'.format(s))
        print('Seu alistamento foi em {}'.format(a))
else:
    print('Você não é obrigada a se alistar! Mas sinta-se convidada a fazer o alistamento.')
