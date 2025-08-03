import re

operação = input('Qual a operação?')
conta = re.search(r'(\d)+(\+|\-|\*|\/)+(\d)$', operação)

a = float(conta.group(1));
b = str(conta.group(2));
c = float(conta.group(3));

if b == '+':
    resultado = a + c

elif b == '-':
    resultado = a - c

elif b == '*':
    resultado = a * c

else:
    resultado = a / c
    

print(f'O resultado é: {resultado}')