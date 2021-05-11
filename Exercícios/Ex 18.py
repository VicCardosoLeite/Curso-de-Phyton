import math
a=float(input('Digite o ângulo: '))
seno= math.sin(math.radians(a))
cos= math.cos(math.radians(a))
tang= math.tan(math.radians(a))
print('Esse ângulo tem o seno igual a {:.2f}, o cosseno é {:.2f} e a tangente tem valor {:.2f}'.format(seno,cos,tang))



