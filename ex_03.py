# 3) Sabe-se que para iluminar de maneira correta os cômodos de uma casa, para cada metro
#   quadrado de área deve-se usar 18 watts de potência. Desenvolva um programa que receba as
#   dimensões de dois lados de uma casa (em metros), calcule a área da casa (A = lado * lado), e
#   mostre quantos watts serão necessários para iluminar corretamente esta casa.

ladoA = int(input("Quanto mede o comprimento do cômodo da casa: "))
ladoB = int(input("Quanto mede o comprimento do cômodo da casa: "))

area = a * b

qtdeWatts = area * 18

print(f"O número de watts usado é de {qtdeWatts:.0f}")