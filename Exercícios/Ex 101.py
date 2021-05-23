from datetime import date
def voto(ano_de_nascimento):
    atual = date.today().year
    idade = atual - ano_de_nascimento
    if idade < 16:
        return f'Como a pessoa tem {idade} anos ela não pode votar!!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Como a pessoa tem {idade} anos o voto é opcional!!'
    else:
       return f'Como a pessoa tem {idade} anos o voto é obrigatório!!'


nasc = int(input('Em que ano a você nasceu? R: '))
print(voto(nasc))
