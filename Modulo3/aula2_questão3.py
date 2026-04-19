idade = int(input("Digite sua idade: "))
jogou3 = input("Já jogou pelo menos 3 jogos? (True/False): ")
vitorias = int(input("Quantas vezes você venceu? "))

jogou3 = jogou3 == "True"

resultado = (16 <= idade <= 18) and jogou3 and (vitorias >= 1)

print(resultado)
