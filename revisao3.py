#Peça ao usuário um número e diga se ele é positivo, negativo ou igual a zero.

numero = int(input("Digite um número: "))

if numero > 0:
    print("Número positivo")
elif numero == 0:
    print("Número igual a zero")
else:
    print("Número negativo")