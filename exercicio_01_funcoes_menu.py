def exibir_menu():
    print (f"""\n
    ====== MENU ======
    1 - Saudação
    2 - Sobre
    3 - Ajuda
    0 - Sair
    ====== ==== ======
    """)
    
    opcao = input("Escolha uma opção: ")
    return opcao

def saudacao():
    print(f"Olá, {nome}! Bem-vindo ao curso Jovem Programador!")

def sobre():
    print("Curso básico para iniciantes.")

def ajuda():
    print("Esse exercício ajuda a entender como uma função funciona.")

nome = input("Qual o seu nome? ")

while True:
    opcao = exibir_menu()
    if opcao == "0":
        print("Programa encerrado.")
        break

    if opcao not in ["1", "2", "3", "4", "0"]:
        print("Opção inválida. Tente novamente.")
        continue

    if opcao == "1":
        saudacao()
    
    elif opcao == "2":
        sobre()

    elif opcao == "3":
        ajuda()