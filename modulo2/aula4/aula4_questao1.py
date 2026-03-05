#O terreno possui 250m2 e custa R$512,490.50
#area_m2 = comprimento * largura
#preco_total = preco_m2 * area_m2
comprimento = int(input("Qual o comprimento? "))
largura = int(input("Qual a largura? "))
preco_m2 = float(input("Qual o valor por metro quadrado? "))

aream2 = comprimento * largura
preco_total = aream2 * preco_m2

print("A área total é", aream2)
print("O preço total é R$", preco_total)