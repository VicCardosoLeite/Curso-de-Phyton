#Função(parte 2)
#Interactive help:
#Para usar se usa help()
#Serve para te ajudar quando tiver uma dúvida sobre algum comando
#Ex: help(print)
#Docstrings
#Serve para criar um "manual" para a sua função
#Para fazer um doc faz assim:
def cont(i,f,p):
    """
    -> Contagem:
    i = início
    f = fim
    p = passo 
    """
help(cont)
print('-=-'*20)
#Parâmetros opcionais:
#É parecido com o * (aparece na aula anterior)
#Faz assim:
#def somar(a,b,c=0):, pode ser assim também, def somar(a=0,b=0,c=0):
#Escopo de variáveis:
#É a área onde a variável funciona
#Retorno de valores:
#Para se utiliar faz assim:
def somar(a=0,b=0,c=0):
    soma = a + b + c
    return soma
s1 = somar(3,2,5)
s2 = somar(7,2)
print(f'Meus cálculos deram {s1} e {s2}')
print('-=-'*20)
#Parte prática
def fatorial(número = 1):
    f = 1
    for c in range(número, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}')
print('-=-'*20)
def par(número = 0):
    if número % 2 == 0:
        return True
    else:
        return False

núm = int(input('Digite um número: '))
print(f'{núm} é par? R: {par(núm)}')
