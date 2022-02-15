'''9-Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''


casa = int(input('insira o valor da casa:\n'))
salario = int(input('insira o salario do comprador:\n'))
anos = int(input('insira em quantos anos ele vai pagar:\n'))

prestaçao = casa / (anos * 12)

if prestaçao > salario * 30 / 100:
    print(f'emprestimo bancario negado')
else:
    print(f'emprestimo aceito')