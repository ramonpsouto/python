a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
op = input('Qual cálculo você deseja fazer? [+, -, *, /, **]: ')

def calcular():
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b
    if op == '**':
        return a ** b

print(a, op, b, '=', calcular())