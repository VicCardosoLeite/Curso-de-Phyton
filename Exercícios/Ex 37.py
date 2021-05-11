n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
(1) Binária
(2) Octal
(3) Hexadecimal''')
select = input('Sua opção: ')
if select == '1':
    print('{} convertido para binário é {}.'.format(n, bin(n)[2:]))
elif select == '2':
    print('{} convertido para octal é {}'.format(n, oct(n)[2:]))
elif select == '3':
    print('{} convertido para hexadecimal é {}.'.format(n, hex(n)[2:]))
else:
    print('Opção inválida, tente novamente')
