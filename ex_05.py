# 5) Faça um programa que leia um número de até três dígitos, calcule e imprima a soma dos seus dígitos.
# Exemplo: 123 = 1 + 2 + 3 = 6.

numero = int(input("Insira um número de 3 dígitos: "))

primNum = numero % 100
segNum = numero % 10
tercNum = numero % 1

numTotal =