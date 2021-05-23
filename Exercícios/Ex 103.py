def ficha(nome='<desconhecido>',gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


jogador = str(input('Digite o nome do jogador: '))
quant_gols = str(input('Digite quantos gols esse jogador fez: '))
if quant_gols.isnumeric():
    quant_gols = int(quant_gols)
else:
    quant_gols = 0
if jogador.strip() == '':
    ficha(gols=quant_gols)
else:
    ficha(jogador,quant_gols)
