'''5-Escreva um programa que Receba um número pelo teclado, se o numero for positivo calcule e mostre
sua raiz quadrada, se for negativo passe uma mensagem informando valor inválido'''

valor = int(input('insira um valor para verificar:\n'))
if valor >= 0:
    print(f'{valor ** 0.5 }')
else:
    print(f'o valor é inválido ')