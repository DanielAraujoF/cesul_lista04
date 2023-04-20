# 4) Faça um programa para calcular a quantidade de barbante necessária, em centímetros, para amarrar um pacote com
# duas voltas de barbante sendo uma pela largura e outra pelo comprimento. Serão fornecidas a largura, a altura e o
# comprimento do pacote. Para amarrar as pontas do barbante são necessários 10 cm de barbante em cada ponta.

alt = float(input("Informe a altura da caixa: "))
larg = float(input("Informe a largura da caixa: "))
comp = float(input("Informe o comprimento da caixa: "))

barbLarg = (alt * 2) + (larg * 2) + 10
barbComp = (alt * 2) + (larg * 2) + 10

totalBarb = barbComp + barbLarg

print(f"O comprimento de barbante a ser usado é {totalBarb:.2f}")

# no lugar das linhas 9-12, poderia ter sido feito assim:
# totalBarbanteUsado = (((altura * 2) + (largura * 2)) + ((altura * 2) + (largura * 2))) + 20
