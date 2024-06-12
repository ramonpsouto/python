num = int(input("Digite um número para ser o fim da sequência, enquanto os 10 primeiros serão múltiplos de 3: "))
x = 1

while x < 11: #exibe os 10 primeiros números multiplicados por 3
    print(x * 3)
    x += 1
while x <= num: #exibe os números normais enquanto não atingir o fim da sequência
    print(x)
    x += 1