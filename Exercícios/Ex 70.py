cont1 = 1
produto1000 = tot = menor = cont2 = 0
quant = int(input('Quantos produtos você comprou? R: '))
barato = ' '
while True:
    cont1 += 1
    print('-'*30)
    produto = str(input(f'Qual o nome do produto? R: ')).strip()
    preço = float(input('Quanto ele custou? R$ '))
    cont2 += 1
    tot += preço
    if preço > 1000:
        produto1000 += 1
    if cont2 == 1 or preço < menor:
        menor = preço
        barato = produto
    if cont1 > quant:
        break
print('-'*30)
print(f'O total foi R${tot:.2f}.')
print(f'Tem {produto1000} produtos que custam mais de R$1000.')
print(f'O produto mais barato custa R${menor:.2f} e foi {barato} .')
print('-'*30)
print('Fim!!!')
