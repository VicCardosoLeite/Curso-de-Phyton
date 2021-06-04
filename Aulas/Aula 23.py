#Tratamento de erros e exceções
try:
    a = int(input('Numerador: '))
    b = int(input('Divisor: '))
    r = a / b
#except Exception as erro:
    #print(f'Infelizmente tivemos problema ;-; !O problema foi {erro.__class__}')
except (ValueError,TypeError):
    print('Tivemos problemas com os tipos dos dados fornecidos ;-;')
except ZeroDivisionError:
    print('Não é possível dividir um número por 0')
except KeyboardInterrupt:
    print('O usuário não forneceu os dados!')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre!Muito Obrigada')
