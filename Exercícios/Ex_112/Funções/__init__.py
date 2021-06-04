def aumentar(preço = 0,taxa = 0,formatação=False):
    resultado = preço + (preço * taxa/100)
    return resultado if formatação is False else moeda(resultado)

def diminuir(preço = 0,taxa = 0,formatação=False):
    resultado = preço - (preço * taxa/100)
    return resultado if formatação is False else moeda(resultado)

def dobro(preço = 0,formatação=False):
    resultado = preço * 2
    return resultado if formatação is False else moeda(resultado)

def metade(preço = 0,formatação=False):
    resultado = preço / 2
    return resultado if formatação is False else moeda(resultado)

def moeda(preço = 0,moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def organiza(preço=0, taxaaumento=10,taxadiminuir=15):
    print('---'*20)
    print(f'Valor analizado: {moeda(preço)}'.center(20))
    print('---'*20)
    print(f'Dobro do valor: \t{dobro(preço,True)}')
    print(f'Metade do valor:\t{metade(preço,True)}')
    print(f'Aumentando o valor: \t{aumentar(preço,taxaaumento,True)}({taxaaumento}% de aumento)')
    print(f'Diminuindo o valor: \t{diminuir(preço,taxadiminuir,True)}({taxadiminuir}% de diminuição)')
    print('---'*20)
