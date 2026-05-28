"""
#while e True - Menus interativos em Python

=======================================
# 1. Mostra o menu
print("=== MENU ===")
print("1 - Opção A")
print("0 - Sair")

# 2. Lê a escolha
opcao = input("Escolha: ")

# 3. Executa ou sai
if opcao == "0":
    break
=======================================

Entra no loop: while True: 
Exibe o menu: print("-----")
Lê a escolha: input("------")
Executa a ação: if / elif / else
Sair: break

"""

while True:
    
    print("=== Calculadora ===")
    print("1 - soma (+)")
    print("2 - subtração (-)")
    print("3 - multipplicação (x)")
    print("4 - divisão (/)")
    print("0 - sair")
    print("-------------------")

    escolha = input("Escolha uma opção: ")

    if escolha == "0":
        print("Programa encerrado.")
        break

    if escolha not in ["1", "2", "3", "4", "0"]:
        print("Opção inválida. Tente novamente.")
        continue

    numero_1 = int(input("Digite um valor: "))
    numero_2 = int(input("Digite outro valor: "))

    if escolha == "1":
        calculo = numero_1 + numero_2
        print(f"A soma de {numero_1} + {numero_2} é de: {calculo}")

    elif escolha == "2":
        calculo = numero_1 - numero_2
        print(f"A subtração de {numero_1} e {numero_2} é de: {calculo}")

    elif escolha == "3":
        calculo = numero_1 * numero_2
        print(f"A multipicação de {numero_1} e {numero_2} é de: {calculo}")

    elif escolha == "4":
        if numero_2 == 0:
            print("Não é possível dividir por zero")
        else: 
            calculo = numero_1 / numero_2
            print(f"A divisão de {numero_1} e {numero_2} é de: {calculo}")
        