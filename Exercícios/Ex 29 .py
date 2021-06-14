v = float(input('Qual a velocidade do carro? R: '))
if v<= 80:
    print('\033[0;32mTenha um bom dia! Dirija com cuidado!\033[m')
else:
    print('\033[0;31mMULTADO!\033[m Você excedeu o limite da via que é \033[0;32m80Km/h\033[m')
    m = (v - 80) * 7
    print('Sua multa é de \033[0;31mR${:.2f}'.format(m))
