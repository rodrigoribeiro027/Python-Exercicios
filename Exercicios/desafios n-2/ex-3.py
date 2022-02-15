'''3-Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

passagem = 0
distancia = float(input('qual a distância da sua viagem em kilometros?\n'))
if distancia <= 200:
    passagem = distancia * 0.45
else: 
    passagem = distancia * 0.50
print(f'a passagem vai custar R${passagem:.2f} Reais.')    

