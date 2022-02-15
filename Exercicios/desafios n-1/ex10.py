'''10- Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado.
Calcule o pre�o a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''
km = float(input('insira a quantidade de kms rodados: '))
dias_alugado = int(input('insira a quantidade de dias alugados:'))
total = km * 0.15 + dias_alugado * 60 
print(f'o carro foi alugado por {dias_alugado}dias.\n o carro rodou por {km}rodados \n o preço total a pagar pelos dias e pelos quilometros percorridos foi {total} Reais.')