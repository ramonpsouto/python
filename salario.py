salario = int(input("Qual seu salário? "))

if salario > 1250:
    aumento = salario / 100 * 10
else:
    aumento = salario / 100 * 15

print("Aumento de R$", aumento)