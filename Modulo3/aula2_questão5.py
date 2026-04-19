genero = input("Digite seu gênero (M ou F): ")
idade = int(input("Digite sua idade: "))
tempo = int(input("Digite seu tempo de serviço (em anos): "))

pode_aposentar = (
    ((genero == "F" or genero == "f") and idade > 60) or
    ((genero == "M" or genero == "m") and idade >= 65) or
    (tempo >= 30) or
    (idade >= 60 and tempo >= 25)
)

print(pode_aposentar)
