velocidade = int(input("Em qual velocidade o carro estava? "))
multa = (velocidade - 80) * 5

if velocidade > 80:
    print("Você ultrapassou o limite de velocidade. Multa: R$", multa, ". Faça o pix: 15 99188-1471")
else:
    print("Você não ultrapassou o limite de velocidade.")