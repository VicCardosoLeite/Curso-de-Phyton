def dinheiro(mensagem):
    válido = False
    while not válido:
        entrada =str (input(mensagem)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO!!{entrada} é inválido! Tente novamente\033[m')
        else:
            válido = True
            return float(entrada)
