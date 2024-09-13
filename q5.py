valor_saque = int(input("Digite o valor do saque (em reais): "))
notas_50 = valor_saque // 50
valor_saque %= 50
notas_10 = valor_saque // 10
valor_saque %= 10
notas_1 = valor_saque // 1
print("Valor do saque: ", end="")
print(notas_50 * 50 + notas_10 * 10 + notas_1)
print("Quantidade de notas de R$50: ", notas_50)
print("Quantidade de notas de R$10: ", notas_10)
print("Quantidade de notas de R$1: ", notas_1)