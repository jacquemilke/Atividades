#a repetição continua "enquanto" a condição for verdadeira.
#sintaxe
#while condicao:

contador = 1
while contador <= 5:
    print("Contator: ", contador)
    contador += 1

while True:
    resposta = input("Digite 'sair' para encerrar: ")
    if resposta == "sair":
        break

