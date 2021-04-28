s = str(input('Informe seu sexo(M/F): ')).strip().upper()[0]
while s not in 'Mm Ff':
    str(input('Inválido! Por favor digite novamente seu sexo: ')).strip().upper()[0]
i = int(input('Informe sua idade: '))
print('Dados registrados com sucesso! Obrigada pela sua colaboração!')