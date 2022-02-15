'''2-Faça um programa que leia um nome e mostre na tela ao contrario em Minúsculo'''
nome = str(input('insira seu nome:\n ')).strip()
print(f'O nome {nome} ao contrario fica: {nome[::-1].lower()} ')