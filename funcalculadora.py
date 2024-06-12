def soma(a, b):
    return a +  b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    return a / b

def calculadora(a, b, operacao):
    if operacao == '+':
        return soma(a, b)
    elif operacao == '-':
        return subtracao(a, b)
    elif operacao == '*':
        return multiplicacao(a, b)
    elif operacao == '/':
        return divisao(a, b)
    else:
        return 'Operação inválida'

print(calculadora(2, 3, '+'))
print(calculadora(20, 33, '-'))
print(calculadora(15, 78, '*'))
print(calculadora(94, 64, '/'))
print(calculadora(94, 64, 's'))