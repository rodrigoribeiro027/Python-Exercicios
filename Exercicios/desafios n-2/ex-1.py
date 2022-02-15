'''1- Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''
import random
velocidade = random.randint(0,100)
print(f'O carro esta a {velocidade} quilometros por/h.\n')

if velocidade > 80:
    print(f'Seu veiculo esta sendo multado por excesso de velocidade.')
    print(f'A multa vai custar a cada R$7,00 por cada Km acima do limite. Então sua velocidade foi {velocidade} o total a pagar sera de {(velocidade - 80) * 7} Reais.')
elif velocidade < 80:
    print(f'voce esta no limite de velocidade') 