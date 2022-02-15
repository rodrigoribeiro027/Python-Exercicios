'''
6- Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice-versa. Por exemplo: OSSO e OVO são palíndromos.
Faça um programa que leia UMA palavra e verifique se é palíndromo, neste programa não consideramos os espaços, apenas UMA PALAVRA.'''

palavra = str(input('insira uma palavra:\n ')).strip().lower()
print(f'a palavra escolida foi {palavra} a palavra ao contrario fica {palavra[::-1]}')

if palavra == palavra [::-1]:
    print(f'é palíndromo')
else:
    print(f'nao é palíndromo')