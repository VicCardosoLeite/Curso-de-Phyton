def situação_da_classe(* notas,situação = False):
    boletim = dict()
    boletim['Total de notas'] = len(notas)
    boletim['Maior nota'] = max(notas)
    boletim['Menor nota'] = min(notas)
    boletim['Média da turma'] = sum(notas)/len(notas)
    if situação == True:
        if boletim['Média da turma'] <= 5:
            boletim['situação'] = 'RUIM'
        elif 6 <= boletim['Média da turma'] < 7:
            boletim['situação'] = 'RAZOÁVEL'
        else:
            boletim['situação'] = 'BOA'
    return f'''
-Ao todo foram cadastradas {boletim["Total de notas"]} notas. 
-A maior foi: {boletim["Maior nota"]}
-A menor foi: {boletim["Menor nota"]}   
-A média da turma é {boletim["Média da turma"]:.1f}
-A situação da turma é: {boletim["situação"]}'''


#Programa principal
print(situação_da_classe(10,9.7,8.4,3.7,5.6,situação=True))
