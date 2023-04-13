# 8) Uma loja está realizando um levantamento a respeito das pendências financeiras dos seus
#   clientes. A ideia é levantar o percentual de clientes que se enquadram em cada uma das
#   seguintes situações:
#   • Clientes isentos de pendências
#   • Clientes com parcelas em dia e
#   • Clientes com parcelas em atraso.

clientesIsentos = int(input("Quantos clientes estão isentos de dívidas?"))
clientesEmDia = int(input("Quantos clientes estão em dia?"))
clientesAtrasados = int(input("Olá, quantos clientes estão atrasados com seus débitos?"))

totalDeCLientes = clientesIsentos + clientesAtrasados + clientesEmDia

porcentagemIsentos = ((clientesIsentos * 100) / totalClientes)
porcentagemEmDia = ((clientesEmDia * 100) / totalClientes)
porcentagemAtrasados = ((clientesAtrasados * 100) / totalClientes)

print(f"A porcentagem de clientes com dívidas atrasadas é {clientesAtrasados:.0f}%, a porcentagem de clientes em dia com suas dívidas é de {clientesEmDia:.0f}% e a porcentagem de clientes isentos de dívidas é de {clientesIsentos:.0f}%.")