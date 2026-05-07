frutas = ["maça", "banana", "abacaxi", "laranja", "uva"]

fruta_favorita = input("Qual a sua fruta favorita? ")

#se a fruta favorita não está na lista frutas
if fruta_favorita not in frutas:
    print(f"Sua fruta favorita não foi encontra da lista. Adicionando...")
    frutas.append(fruta_favorita)
    
#para cada posição (índice) e fruta na lista numerada
for posicao, fruta in enumerate(frutas):
    #faça isso:
    #se a fruta dessa iteração é igual a fruta favorita
    if fruta == fruta_favorita:
        #salva numa nova variável a posição dessa iteração
        posicao_fruta_favorita = posicao
        #quebra o for (faz ele parar)
        break

print(f"Minha fruta favorita está na posição índice {posicao_fruta_favorita}")

