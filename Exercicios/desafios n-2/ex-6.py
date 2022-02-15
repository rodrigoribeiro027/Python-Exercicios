'''6-Desenvolva um programa que leia o comprimento de três retas e 
diga ao usuário se elas podem ou não formar um triângulo.'''
reta1 = float(input('insira o valor da reta1:\n'))
reta2 = float(input('insira o valor da reta2:\n'))
reta3 = float(input('insira o valor da reta3:\n'))

if reta1 > reta2 + reta3:
    print(f'não forma um triângulo.')
elif reta2 > reta1 + reta3:
    print(f'não forma um triângulo.')
elif reta3 > reta1 + reta2:
    print(f'não forma um triângulo.')
else:
    print(f'formou um triangulo')