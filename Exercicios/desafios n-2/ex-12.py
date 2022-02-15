'''12 -Faça um programa que receba a altura e o sexo de uma pessoa, calcule e mostre seu peso ideal, utilizando
a seguinte fórmulas(onde h corresponde á altura):
  ºHomens (72.7*h) - 58
  ºMulheres (62.1*h) - 44.7'''
peso_ideal = 0
altura = float(input('insira a altura:\n'))
sexo = str(input('insira o sexo M/F:\n'))

if sexo == 'm':
  peso_ideal = altura * 72.7 - 58
else:
  peso_ideal = altura * 62.1 - 44.7
print(f'tendo como base a altura {altura} e peso ideal do individuo é {peso_ideal:.2f}')