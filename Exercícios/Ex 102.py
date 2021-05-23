def fatorial(num,show = False):
    """
    Objetivo -> Mostra o fatorial de um numero
    Parâmetros -> .num = numero que deve ser feito o fatorial
                    Exemplo: print(fatorial(5))
                    O programa vai mostrar 120
                  .show = por ele vem com o valor False, mas se você
                    mudar isso para True, o programa vai mostrar não só o resultado 
                    mas a conta também.
    """
    fat = 1
    for c in range(num, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(f' x ',end='')
            else:
                print(f' = ',end='')
        fat*=c
    return fat


print(fatorial(5, show=True))
print()
print(help(fatorial))
