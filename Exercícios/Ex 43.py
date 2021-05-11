from time import sleep
peso = float(input('Informe o seu peso(Kg): '))
alt = float(input('Informe sua altura(m): '))
print('')
print('Calculando IMC...')
print('')
sleep(3)
imc = peso / (alt ** 2)
print('Seu IMC é {:.1f}.'.format(imc))
print('')
print('Vendo sua faixa...')
sleep(3)
if imc < 18.5:
    print('Você está abaixo do peso ideal, recomendo procurar um nutricionista!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal, mas continue com o acompanhamento médico!')

elif 25 <= imc < 30:
    print('Você está com sobrepeso, atenção! Procure ajuda médica assim que possível!')
elif 30 <= imc < 40:
    print('Você está com obesidade! Procure ajuda médica o mais rápido possível!!')
else:
    print('Você está com obesidade mórbida!! Procure ajuda IMEDIATAMENTE!!!')