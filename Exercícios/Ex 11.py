lado = float(input('Qual a largura da sua parede? Resposta: '))
altura = float(input('Qual a altura da sua parede? Resposta: '))
área = lado * altura
tinta = área / 2
print(f'Sua parede de {lado}x{altura} tem {área}m² de área!')
print(f'Para pinta-la vai precisar de {tinta}L de tinta!')
