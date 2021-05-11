#Funções:
#Função está ligada a rotina
#Ex: print(),len(),input(),int(),float()
#São coisas que você faz constantemente durante seus programas
#Para fazer uma função:
#def mostralinha(): Todas as funções terminam com ()!
#    print('-=-'*20)
def linhas():
    print('-=-'*20)
#Programa principal
linhas()
print('Aprenda Phyton')
linhas()
print('Olá')
linhas()
print('Vic')
linhas()
print()
#Parametros
def título(txt):
    print('---'*20)
    print(txt)
    print('---'*20)
#Programa princial
título('Oi')
título('Sou program')
título('Aprendendo')
print()
#Empacotando parametros
def cont(* núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são {tam} números!')

cont(8,9,4,6)
cont(4)
cont(8,5,6,9,7,3,4,2)
print()
#Com lista
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [4,2,3,6]
dobra(valores)
print(valores)
