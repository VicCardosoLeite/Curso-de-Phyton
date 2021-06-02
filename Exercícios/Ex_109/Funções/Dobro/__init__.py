def dobro(preço = 0,formatação=False):
    resultado = preço * 2
    return resultado if formatação is False else moeda(resultado)
    