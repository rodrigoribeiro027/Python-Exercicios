'''
8-Escreva um programa que, receba dois inteiros e mostre o maior valor, e a diferença entre eles,
se forem iguais mostre uma menssagem.'''
valor1 = int(input('insira um valor:\n'))
valor2 = int(input('insira outro valor:\n'))
if valor1 == valor2:
    print(f'os numeros sao iguais.')
elif valor1 > valor2:
    print(f'a diferença entre {valor1} E {valor2} é de {valor1 - valor2 }')
elif valor2 > valor1:
    print(f'a diferença entre {valor1} E {valor2} é de {valor2 - valor1 }')
