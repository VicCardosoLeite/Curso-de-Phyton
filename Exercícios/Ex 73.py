times =	('Palmeiras', 'Flamengo', 'Internacional','Grêmio','São Paulo',
        'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo',
        'Santos', 'Bahia', 'Fluminense', 'Corinthians',
        'Chapecoense', 'Ceará', 'Vasco', 'Sport',
        'América-MG', 'Vitória', 'Paraná')
print('-=-'*20)
print(f'Lista de times: {times}')
print('-=-'*20)
print(f'Os 5 primeiro são: {times[0:5]}')
print('-=-'*20)
print(f'Os 4 últimos são {times[-4:]}')
print('-=-'*20)
print(f'Os times em ordem alfabética fica: {sorted(times)}')
print('-=-'*20)
print(f'O chapecoense está na {times.index("Chapecoense")+1}ºposição')