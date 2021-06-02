def diminuir(preço = 0,taxa = 0,formatação=False):
    resultado = preço - (preço * taxa/100)
    return resultado if formatação is False else moeda(resultado)
    