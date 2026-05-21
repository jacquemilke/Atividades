#faça um laço for utilizando o range() para exibir a tabuada do 5, começando do 1 e indo até o 10.


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