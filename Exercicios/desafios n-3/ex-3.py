'''3- Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

nome = str(input('insira seu nome:\n ')).strip()

print(f'Maiúsculo {nome.upper()}\n nome minusculo {nome.lower()}')
print(f'ao todo o {nome.capitalize()} tem {len(nome) - nome.count(" ")} letras')
print(f'o primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras')