#Desenvolva um programa que leia 4 números e os guarde em uma tupla. No final mostre:
#a) Quantas vezes o valor nove apareceu
#b) Em que posição foi digitado o primeiro valor 3
#c) Quais foram os números pares
núm = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'Os valores digitados foram: {núm}')
#Letra a):
print(f'O 9 apareceu {núm.count(9)} vezes.')
#Letra b):
if 3 in núm:
    print(f'O 3 apareceu na {núm.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado nenhuma vez.')
#Letra c):
for n in núm:
    if n % 2 == 0:
        print(f'Os valores pares digitados foram {n}')
        