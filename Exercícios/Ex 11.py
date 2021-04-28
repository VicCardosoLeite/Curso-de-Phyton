l=float(input('Qual a largura da sua parede? Resposta: '))
a=float(input('Qual a altura da sua parede? Resposta: '))
área= l*a
tinta= área / 2
print('Sua parede tem {}x{} e a área de {}m². E para pinta-la vai precisar de {}l de tinta'.format(l,a,área,tinta))