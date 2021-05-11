valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    select = str(input('Deseja cotinuar?[S/N] R: ')).strip()
    if select in 'Nn':
        break
print('-=-'*20)
print(f'Você digitou {len(valores)} valores!')
valores.sort(reverse=True)
print(f'Esses valores em ordem decrescente ficam: {valores}.')
if 5 in valores:
    print('E o valor 5 faz parte da lista!')
else:
    print('O 5 não foi encontrado!')
