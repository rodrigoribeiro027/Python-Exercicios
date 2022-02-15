'''13- Receba a temperatura em Graus Celsius e apresente-a convertida em graus Fahrenheit.
formula F=C*(9/5)+32'''
celcius = float(input('insira a temperatura em graus celcius:\n'))
fahrenheit = celcius * 1.8 + 32 
print(f' {celcius}. \n convertidos em fahrenheit é {fahrenheit}.')
