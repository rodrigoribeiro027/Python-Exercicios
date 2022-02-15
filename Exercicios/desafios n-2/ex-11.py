'''11-Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''


valor = float(input('insira o valor do produto:\n'))

controle = int(input('''
Escolha a forma de pagamento /Valor do produto {valor}

[1] -A vista 
[2] - Parcelado 

'''))
if controle == 1:
    controle = int(input('''
[1]- dinheiro/cheque: 10% de desconto
[2] - no cartão: 5% de desconto

'''))
    if controle == 1:
        print(f'com 10% de desconto voce paga {valor - valor * 10/100:.2f}')
    if controle == 2:
        print(f'com 5% de desconto voce paga {valor - valor * 5/100:.2f}')
elif controle == 2:
    controle = int(input('''
[1]- 2x no cartão sem juros 
[2] - 3x ou mais no cartão: 20% de juros

'''))
    if controle == 1:
        print(f'Parcelando em 2x voce nao paga juros. apenas parcelas de {valor / 2 } ')
    if controle == 2:
        print(f'Parcelando em 3x voce paga juros de 20% totalizando {valor + valor *20/100:.2f}\n pagando parcelas de {(valor + valor * 20 / 100) /3}')