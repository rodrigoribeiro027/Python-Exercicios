'''
4- Faça um programa que leia uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, i, o.'''

frase = str(input('insira uma frase:\n ')).strip()

print(f' {frase} , \n')
print(f'na frase temos {frase.count(" ")} espaços vazios')
print(f' a vogal a aparece {frase.count("a")} vezes na frase')
print(f' a vogal o aparece {frase.count("o")} vezes na frase')
print(f' a vogal i aparece {frase.count("i")} vezes na frase')

