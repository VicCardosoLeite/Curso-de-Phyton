m = 0
mn = 0
for c in range(1,6):
    p = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        m = p
        mn = p
    else:
        if  p > m:
            m = p
        if p < mn:
            mn = p
print('')
print('O maior peso lido foi {}Kg'.format(m))
print('E o menor foi de {}Kg'.format(mn))
