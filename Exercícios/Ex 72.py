cont = ('zero','um','dois','três','quatro',
        'cinco','seis','sete','oito','nove',
        'dez', 'onze','doze','treze','quartoze',
        'quinze','dezesseiz','dezesete','dezoito',
        'dezenove','vinte')
resp = ''
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    print ( f'Você digitou o número {cont[núm]}' )
    resp = str(input('Deseja continuar?(S/N) R: ')).strip().upper()[0]
    if resp == 'N':
        break



