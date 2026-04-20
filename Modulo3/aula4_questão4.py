distancia = float(input("Digite a distância em quilômetros: "))
peso = float(input("Digite o peso em quiloramas: "))

if distancia <= 100:
    valor = peso * 1 

elif distancia >= 101 and distancia <= 300:
    valor = peso * 1.50

else: 
    valor = peso * 2

if peso > 10:
    valor = valor + 10

print("O valor do frete é R$ ", valor)
