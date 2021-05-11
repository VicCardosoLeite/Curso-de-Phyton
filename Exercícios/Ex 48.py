soma = 0
contr = 0
for cont in range(1,501,2):
    if cont % 3 == 0:
        contr = contr + 1
        soma = soma + cont
print('A soma dos {} valores é {}.'.format(contr,soma))
