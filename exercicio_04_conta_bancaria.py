def exibir_menu():
    print (f"""\n
    ====== CONTA BANCÁRIA ======
    1 - Depositar
    2 - Sacar
    3 - Ver saldo
    0 - Sair
    =============================
    """)
    
    opcao = input("Escolha uma opção: ")
    return opcao

saldos = 0.0

def depositar():
    add_deposito = float(input("Digite o valor a ser depositado: "))
    saldos.append(add_deposito)
    print(f"O depósito de R$ {add_deposito} foi adicionado com sucesso..")

def sacar():
    if saldos == 0:
        print("==== Não há saldo suficiente para sacar. ====")

    else:
        remove_saldo = int(input(f"Digite o valor que deseja sacar: "))
        
        saldos.pop(remove_saldo -1)
        print("==== O valor foi sacado. ====")

def ver_saldo():
    if not saldos:
        print("==== Não há saldo para listar. ====")

    else:
        print(f"Essa é o seu saldo: ")
        for i, saldo in enumerate(saldos):
            print(f"{i+1} - {saldo}")

while True:
    opcao = exibir_menu()
    if opcao == "0":
        print("==== Programa encerrado. ====")
        break

    if opcao not in ["1", "2", "3", "0"]:
        print("==== Opção inválida. Tente novamente. ====")
        continue

    if opcao == "1": depositar()

    if opcao == "2": sacar()

    if opcao == "3": ver_saldo()