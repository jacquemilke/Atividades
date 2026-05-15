#O usuário digita números até digitar 0. Conte quantos números foram digitados (sem contar o zero).
# Portugol

#contador recebe zero
#numero recebe -1
#se quiser salvar os número digitados, salva uma lista vazia: numeros recebe ista vazia
#enquanto numero for diferente de zero
#pergunte "Digite um número" e converta pra inteiro
#numero recebe o que o usuario digitou
#se numero for diferente de zero
#contador recebe contador +1
#numero é adicionado dentro da lista números
#exibe "Quantidade de tentativas"

contador = 0
numero = -1
numeros = []

while numero != 0:
    numero = int(input("Digite um número: "))

    if numero != 0:
        contador = contador + 1
        

print(f"Quantidade de tentativas: {contador} e os números digitados foram {numeros}!")
