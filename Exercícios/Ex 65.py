cont = 0
resp = 'S'
méd = quant = soma = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar?(S/N) R: ')).strip().upper()
méd = soma / quant
print('A média dos {} valores digitados é {}.'.format(quant, méd))
print('E o maior é {} e o menor é {}.'.format(maior,menor))
