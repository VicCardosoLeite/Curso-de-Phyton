jogador = dict()
partidas = list()
jogador['nome'] = str(input('Digite o nome do jogador: '))
total_partidas = int(input(f'Digite quantas partidas o {jogador["nome"]} jogou: '))
for c in range(0,total_partidas):
    partidas.append(int(input(f'Quantos gols na {c+1}º partida: ')))
jogador['gols'] = partidas[:]
jogador['total de gols'] = sum(partidas)
print('-=-'*20)
print(jogador)
print('-=-'*20)
for k, v in jogador.items():
    print(f'{k} é: {v}')
print('-=-'*20)
print(f'O jogagor {jogador["nome"]} jogou {len(jogador["gols"])} partidas!')
print()
for i,v in enumerate(jogador['gols']):
    print(f'=>Na partida {i+1} ele(a) fez {v} gols.')
print(f'Dando um total de {jogador["total de gols"]} gols!')
