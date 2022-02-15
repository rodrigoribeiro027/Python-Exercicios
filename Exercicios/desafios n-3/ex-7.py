'''7-Faça um programa que leia o nome completo do Usuário e mostre na tela:
* Nome completo
*Primeiro e ultimo nome juntos em apenas uma string
*Nome do meio '''
nome = str(input('insira um nome completo:\n ')).strip()
print(f'o nome completo é {nome}')
print(f' o primeiro e o ultimo nome {nome.split()[0] + " " + nome.split() [len(nome.split()) - 1] }')
print(f'O nome do meio é {nome.split() [len(nome.split()) // 2 ]} ')