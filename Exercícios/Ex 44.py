from time import sleep
print('-=-'*20)
print('LOJAS UM E 99')
print('-=-'*20)
print('')
print('Carregando...')
sleep(3)
p = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO: 
(1) à vista dinheiro/cheque
(2) à vista no cartão
(3) 2x no cartão 
(4) 3x ou mais no cartão''')
select = int(input('Qual a forma de pagamento? R: '))
print('')
print('Processando...')
print('')
sleep(3)
if select == 1:
    t = p - (p * 10 / 100)
    print ( 'O total é R${:.2f}! Obrigado e volte sempre!'.format ( t ) )
elif select == 2:
    t = p - (p * 5 / 100)
    print ( 'O total é R${:.2f}(sem juros)! Obrigado e volte sempre!'.format ( t ) )
elif select == 3:
    t = p / 2
    print('Sua compra será parcelada em 2x.')
    print('Cada parcela será de R${:.2f} ficando R${:.2f} no final. Obrigado e volte sempre!'.format(t,p))
elif select == 4:
    par = int(input('Quantas parcelas? R: '))
    t = p + (p * 20 / 100)
    final = t / par
    print('Sua compra será parcelada em {}x(com juros)')
    print('Ficando R${:.2f} cada parcela e R${:.2f}(com os juros) no final. Obrigada e volte sempre!'.format(par,final,t))
else:
    print('Opção inválida, tente novamente!!')


