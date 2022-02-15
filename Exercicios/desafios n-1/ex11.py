'''11- Crie um programa que receba a IDADE do usuario e imprima na tela quantos meses e dias essa pessoa tem de vida.'''
idade = int(input('insira sua idade:\n'))
meses = 12 * idade
dias = 30 * meses 
print(f'minha idade é {idade}anos \n E tenho {meses} meses de vida.\n Logo tenho {dias} dias de vida.')