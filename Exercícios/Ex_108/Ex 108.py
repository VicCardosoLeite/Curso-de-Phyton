import Funções_do_108
valor = float(input('Digite um valor: R$'))
print(f'A metade do valor informado é: {Funções_do_108.moeda(Funções_do_108.metade(valor))}')
print(f'O dobro do valor informado é: {Funções_do_108.moeda(Funções_do_108.dobro(valor))} ')
print(f'Aumentando 10% fica: {Funções_do_108.moeda(Funções_do_108.aumentar(valor,10))}')
print(f'Diminuindo 15% fica: {Funções_do_108.moeda(Funções_do_108.diminuir(valor,15))}')
