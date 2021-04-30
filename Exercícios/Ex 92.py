from datetime import datetime
cadastro = dict()
cadastro['Seu nome'] = str(input('Digite seu nome: '))
ano = int(input('Digite o ano de nascimento: '))
cadastro['O número da sua carteira'] = int(input('Digite sua ctps(coloque 0 se não tiver): '))
cadastro['Sua idade'] = datetime.now().year - ano
if cadastro['O número da sua carteira'] != 0:
    cadastro['O ano de contratação'] = int(input('Digite o ano de contratação: '))
    cadastro['Seu salário'] = float(input('Digite o salário: R$ '))
    cadastro['Idade com que vai se aposentar'] = cadastro['Sua idade'] + ((cadastro['O ano de contratação'] + 35) - datetime.now().year)
print('-=-'*20)
for k,v in cadastro.items():
    print(f'- {k} é: {v}')
