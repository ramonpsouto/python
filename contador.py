fim = int(input("Digite o último número a imprimir: "))
x = 1

while x <= fim:
  if x % 2 == 0:
    print("Números pares")
    print(x)
    x = x + 1