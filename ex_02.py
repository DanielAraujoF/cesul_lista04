# 2) Considere que para um consórcio sabe-se o número total de prestações, a quantidade de
#   prestações pagas e o valor da prestação. Escreva um programa que determine o valor total pago
#   pelo consorciado e o saldo devedor.

totalParcelas = int(input("Quantas parcelas foi feito? "))
valorParcela = int(input("Qual valor de cada parcela? R$"))
parcelasPagas = int(input("Quantas parcelas já foram pagas? "))

valorTotal = totalParcelas * valorParcela
valorPago = parcelasPagas * valorParcela

valorAPagar = valorTotal - valorPago

print(f"Você já pagou R${valorPago:.0f}, ainda falta R${valorAPagar:.0f}.")