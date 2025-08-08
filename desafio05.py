#Pedir ao usuário que digite dois números
num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))

soma = num1 + num2 
subtr  = num1 - num2 
mult = num1 * num2 
div = num1/num2 
expo = num1**num2 # ** também é exponenciação 

print(f'RESULTADO: Soma dos números: {soma}')
print(f'RESULTADO: Subtração dos números: {subtr}')
print(f'RESULTADO: Multiplicação: {mult}')
print(f'RESULTADO: Divisão dos números^:{div}')
print(f'RESULTADO: Exponenciação dos números:{expo}')