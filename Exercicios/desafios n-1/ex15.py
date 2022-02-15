'''15-  Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''
largura = float(input('insira a largura da parede:\n'))
altura = float(input('insira a altura da parede:\n'))
area = largura * altura 
litros_tinta = area / 2
print(f'a parede tem {altura}de altura e {largura}largura. \n entao sua area total é de {area}\n Para pintar essa parede sera necessario {litros_tinta} litros de tinta para pinta-la. ')