time = list()
jogador = dict()
partidas = list()
while True:  
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    total_partidas = int(input(f'Digite quantas partidas o {jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range(0,total_partidas):
        partidas.append(int(input(f'Quantos gols na {c+1}º partida: ')))
    jogador['gols'] = partidas[:]
    jogador['total de gols'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja adicionar mais um jogador?[S/N] R: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N, por favor.')
    print('-=-'*20)
    if resp == 'N':
        break
print('-=-'*20)
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=-'*20)
for k, v in enumerate(time):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-=-'*20)
while True:
    busca = int(input('Mostrar dados de qual jogador?(999 para parar) R: '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Não existe jogador com esse código, tente novamente.')
    else:
        print(f'--- Levantamento do jogador {time[busca]["nome"]} ---')
        for i, g in enumerate(time[busca]['gols']):
            print(f'Na {i+1}º partida ele fez {g} gols.')
    print('-=-'*20)
print()
('FIM DO PROGRAMA! VOLTE SEMPRE!')
