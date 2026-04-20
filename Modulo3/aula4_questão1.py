numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2 
resultado = soma % 2

if resultado == 0 :
    print("A soma do seu número é par")
else: 
    print("A soma do seu número é impar")
