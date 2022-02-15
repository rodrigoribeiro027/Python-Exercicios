'''10-Uma empresa vende o mesmo produto para quatro estados diferentes. Cada estado possui uma taxa diferente 
de imposto sobre o produto(MG 7%; SP 12%; RJ 15%; MS 8%). Faça um programa em que o usuário entre com o valor 
e o estado destinodo produto e o programa retorne o preço final do produto acrescido do imposto do estado em que ele será vendido. 
Se o estado digitado não for válido, mostre ume mensagem de erro.
'''
valor = float(input('insira o valor do produto:\n'))
destino = str(input('insira o destino\nMG-SP-RJ-RS \n'))

print(f'o bruto do produto Rs: {valor} com ',end='')
if destino == 'mg':
    print(f'7% de aumento fica {valor + valor * 7 /100}')
elif destino == 'sp':
    print(f'12% de aumento fica {valor + valor * 12 /100}')
elif destino == 'rj':
    print(f'15% de aumento fica {valor + valor * 15 /100}')
else:
    print(f'8% de aumento fica {valor + valor * 8 /100}')