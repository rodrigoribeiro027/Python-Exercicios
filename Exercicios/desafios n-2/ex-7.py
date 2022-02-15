'''7-Faça um programa que mostre ao usúario um menu com 4 operações matemáticas, depois
solicite dois valores e realize a operação mostrando os dados na tela.'''
controle = int(input('''Selecione o operador desejado
[1]- Soma
[2]- Subtração
[3]- Divisão
[4]- Multiplicação

 '''))
valor1 = int(input('insira valor 1:\n'))
valor2 = int(input('insira valor 2:\n'))

if controle == 1: 
    print(f'{valor1} + {valor2} = {valor1 + valor2}')
elif controle == 2:
    print(f'{valor1} - {valor2} = {valor1 - valor2}')
elif controle == 3:
    print(f'{valor1} / {valor2} = {valor1 / valor2}')
elif controle == 4:
    print(f'{valor1} * {valor2} = {valor1 * valor2}')