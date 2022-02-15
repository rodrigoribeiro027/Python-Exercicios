'''4-Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario = int(input('qual o seu salario?\n'))
if salario > 1250:
    print(f'Com um aumento de 10% o reajuste no salario foi de: {salario + salario * 10 / 100}\n')
else:
    print(f'Com um aumento de 15% o reajuste no salario foi de: {salario + salario * 15 / 100}\n ')
