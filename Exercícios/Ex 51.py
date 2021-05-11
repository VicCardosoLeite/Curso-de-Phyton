n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = n + (10-1) * r
for c in range(n , d + r, r):
    print('{}'.format(c),end=' -> ')
print('Acabou')