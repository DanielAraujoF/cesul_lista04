# 1) Desenvolva um programa que receba do usuário um valor numérico inteiro x e retorne como
#   saída o resultado da seguinte fórmula: 𝑥² + 10𝑥 − 5

numeroInteiro = int(input("Insira o número que deseja para entrar como a variável x na fórmula '𝑥² + 10𝑥 − 5':"))

resultFormula = numeroInteiro * numeroInteiro + 10 * numeroInteiro - 5

print(f"O resultado da fórmula é {resultFormula:.2f}")