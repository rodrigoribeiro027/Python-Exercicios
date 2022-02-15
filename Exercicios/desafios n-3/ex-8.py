'''8-Leia dois nomes pelo teclado e imprima:
 O maior entre eles(Sem considerar espaços), se forem do mesmo tamanho imprima uma mensagen.
 Quem tem o ultimo nome menor, se forem do mesmo tamanho imprima uma mensagen.
 Nome do meio ao contrario'''

nome1 = str(input('insira seu nome1 :\n ')).strip()
nome2 = str(input('insira seu nome2 :\n ')).strip()
if (len (nome1) - nome1.count(' ')) > (len (nome2) - nome1.count(' ')):
    print(f'O nome {nome1} é maior que o nome {nome2}')
elif (len (nome1) - nome1.count(' ')) < (len (nome2) - nome1.count(' ')):
    print(f'O nome {nome2} é maior que o {nome1}')
else: 
    print(f'os nomes são do mesmo tamanho')

if nome2.split()[len(nome2.split()) - 1] < nome1.split()[len(nome1.split()) - 1]:
    print(f'o nome {nome2.split()[len(nome2.split()) - 1]} é maior que o {nome1.split()[len(nome1.split()) - 1]}')
elif nome1.split()[len(nome1.split()) - 1] > nome2.split()[len(nome2.split()) - 1]:
        print(f'O nome {nome1.split()[len(nome1.split()) - 1]} é maior que o {nome2.split()[len(nome2.split()) - 1]}')
else:
    print(f'os nomes são do mesmo tamanho')

print(f'o nome1 do meio ao contrario {nome1.split() [len(nome1.split()) // 2 ][::-1] } ')
print(f'o nome2 do meio ao contrario {nome2.split() [len(nome2.split()) // 2 ][::-1] } ')