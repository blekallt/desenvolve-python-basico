#Entrada
#Saída
#Digite o nome do produto 1:calça
#Digite o preço unitário do produto 1:199.90
#Digite a quantidade do produto 1: 3
#Digite o nome do produto 2:camisa
#Digite o preço unitário do produto 2:49.95
#Digite a quantidade do produto 2:10
#Digite o nome do produto 3:cinto
#Digite o preço unitário do produto 3:25
#Digite a quantidade do produto 3:3

produto1 = (input("Digite o nome do produto1 "))
preço_p1 = int(input("Digite o preço unitário do produto1 "))
quantidade_p1 = int(input("Digite a quantidade do produto1 "))

Produto2 = (input("Digite o nome do produto2 "))
preço_p2 = int(input("Digite o preço unitário do produto2 "))
quantidade_p2 = int(input("Digite a quantidade do produto2 "))

Produto3 = (input("Digite o nome do produto3 "))
preço_p3 = int(input("Digite o preço unitário do produto3 "))
quantidade_p3 = int(input("Digite a quantidade do produto3 "))

saida1 = preço_p1 * quantidade_p1
saida2 = preço_p2 * quantidade_p2
saida3 = preço_p3 * quantidade_p3

Total = saida1 + saida2 + saida3
print("Total: R$", Total)


