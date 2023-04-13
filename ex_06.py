# 6) Suponha que um caixa disponha apenas de cédulas de R$ 100, 10 e 1. Escreva um programa
#   para ler o valor de uma conta e o valor fornecido pelo usuário para pagar essa conta, e calcule e
#   troco. Calcular e mostrar a quantidade de cada tipo de cédula que o caixa deve fornecer como
#   troco. Mostrar, também o valor da compra e do troco.

valorDaConta = float(input("Insira o valor da conta devida:"))
dineroDadoPeloCliente = float(input("Insira o valor que o cliente entregou para pagar a conta:"))

valorTroco = dineroDadoPeloCliente - valorDaConta

notasDeCem = int(valorTroco / 100)
notasDeDez = int((valorTroco - (notasDeCem * 100)) / 10)
notasDeUm = int((valorTroco - (notasDeCem * 100) - (notasDeDez * 10)) / 1)

print(f"O valor do troco a ser devolvido é de {valorTroco:.0f}")
print(f"O troco possível é de {notasDeCem:.0f} notas de R$100, {notasDeDez:.0f} notas de R$10 e {notasDeUm:.0f} notas de R$1.")
print("Se dever centavos ao cliente, dê em balinhas ;)")