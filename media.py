import math

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

media = round((nota_1 + nota_2 + nota_3) / 3, 2)

"""
ou o roud pode ser usado assim:
media = round(media, 2) - o número depois da vírgula é a quantidade de casas decimais
media = math.ceil(media) - utiliza essa sintaxe para arredondar para cima
media = math.floor(media) - utiliza essa sintaxe para arredondar para baixo
"""

if media >= 7:
    print("Você está aprovado! Sua média é: ", media)

elif media >= 5 and media < 7:
    print("Você está em recuperação! Sua média é: ", media)

else:
    print("Você está reprovado! Sua média é: ", media)