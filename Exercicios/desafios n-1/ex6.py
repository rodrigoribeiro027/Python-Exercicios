'''6- Receba o pre�o de um produto e mostre com 25% de desconto'''
preço = float(input('Insira o valor do produto:\n'))
print(f'o valor do produto é {preço} Reais.\n Com 25% de desconto o valor ficaria {preço - preço*25/100:.2f} Reais')
