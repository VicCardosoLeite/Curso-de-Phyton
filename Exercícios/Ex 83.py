#Crie um progra em que o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
#deverá analisar se a expressão é válida:
expressão = str(input('Digite uma expressão: '))
pilha = list()
for simb in expressão:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else: 
    print('Sua expressão está errada!')
