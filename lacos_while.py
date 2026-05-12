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

while True:
    mensagem = f"""
    Menu:
    1 - Ver sutuação 1
    2 - Ver situação 2
    3 - Sair
    """
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        elif opcao == "2":
            elif opcao == "3":
                print("Sair do sistema...")
                break
    else:
        print("Opção inválida. Tente novamente.")