num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
num3 = int(input('Digite mais um valor: '))
menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<n1 and num3<num2:
    menor = num3
maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
print(f'O menor valor digitado foi {menor} e o maior foi {maior}.')
