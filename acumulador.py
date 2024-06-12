n = 1
soma = 0
x = 0
while x != -1:
    x = int(input('Digite um número: '))
    soma = soma + x #acumulador 
    n = n + 1 #incremento (sempre constante)
    y = y + 1
print(y)
media = soma / n
print('Soma: ', soma)
print('Média: ', media)