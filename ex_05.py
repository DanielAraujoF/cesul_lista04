# 5) Faça um programa que leia um número de até três dígitos, calcule e imprima a soma dos seus dígitos.
# Exemplo: 123 = 1 + 2 + 3 = 6.

numero = int(input("Insira um número de 3 dígitos: "))

primNum = numero / 100
restoPrimNum = numero % 100

segNum = restoPrimNum / 10
restoSegNum = restoPrimNum % 10

tercNum = numero / 1
restoTercNum = restoSegNum % 1

numTotal = restoPrimNum + restoSegNum + restoTercNum

print(f"A soma dos três dígitos do número inserido é {numTotal:.0f}")
