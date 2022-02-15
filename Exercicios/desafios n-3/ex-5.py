'''5-Faça um programa que leia o nome do Usuário e mostre em maiúsculo um em baixo do outro Cinco vezes:
Utilizar apenas DUAS linhas de código, a primeira para ler, a segunda para IMPRIMIR(OBS: Só serar válido se o código tiver apenas um PRINT())

Exemplo-
TADEU
TADEU
TADEU
TADEU
TADEU'''

nome = str(input('insira seu nome:\n ')).strip().upper()
print(f'{nome}\n' * 5)