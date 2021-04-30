nome=input('Qual o seu nome?')
print('Prazer em te conhecer{:=^20}!'.format(nome))
n1=int(input('Um valor:'))
n2=int(input('Outro valor:'))
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('A soma é {}'.format(n1+n2), end=' ')
print('a multiplicação é {},a divisão é {:.1f},a divisão inteira é {} e a potencia é {}'.format(m,d,di,e))