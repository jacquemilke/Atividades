#faça um laço for utilizando o range() para exibir a tabuada do 5, começando do 1 e indo até o 10.

"""
for multiplicador in range(1, 11, 1):
    resultado = multiplicador * 5
    print(f"{multiplicador} x 5 = {resultado}")

#Crie uma lista com vários nomes de cidades e salve ela numa variável de cidades. Faça um laço de repetição for para exibir todos os nomes dessas cidades dessa lista.

cidades = ["Blumenau", "Indaial", "Gaspar", "Pomerode", "Brusque"]

for cidade in cidades:
    #print(cidade)

#agora, use o continue com uma condicional para detectar se a cidade começar com a letra "B", não exibir o nome dela.

    if cidade[0] == "B":
            continue
    else:
        print(cidade)
"""
#Crie uma lista de produtos e outra lista de preços. Use um for para exibir cada nome do produto e o preço dele.
"""
produtos = ["arroz", "feijão", "ovos"]
precos = [5.99, 6.99, 12.99]

for indice, produto in enumerate(produtos):
    print(f"Produto: {produto} custa R$ {precos[indice]}")
   """

#agora, adicione uma lógica que se o produto tem preço menor que R$10 você deverá subir 10% o preço. Mude o print para que a mensagem desses produtos seja diferente, quando essa lógica for aplicada, você deve mostrar o nome, o preço original e o preço atualizado também.

produtos = ["arroz", "feijão", "ovos"]
precos = [5.99, 6.99, 12.99]

for indice, produto in enumerate(produtos):
    if precos[indice] < 10:
        reajuste = round(precos[indice] * 1.10, 2)
        print(f"O produto {produtos[indice]} custava {precos[indice]} e teve o reajuste de 10%. Totalizando R$ {reajuste}")
else:
    print(f"o produto {produto} custa R$ {precos[indice]}")

