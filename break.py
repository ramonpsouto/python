s = 0
while True:
    v = int(input("Digite um número para somar ou 0 para sair: "))
    if v == 0:
        break
    s = s + v
print("Soma: ", s)  