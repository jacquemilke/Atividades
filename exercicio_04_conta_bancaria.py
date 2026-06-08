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

def depositar(saldos):
    add_deposito = float(input("Digite o valor a ser depositado: "))
    saldos = saldos + add_deposito
    print(f"O depósito de R$ {add_deposito} foi adicionado com sucesso.")
    return saldos
    
def sacar(saldos):
    saque = float(input(f"Digite o valor que deseja sacar: "))
    if saque > saldos:
        print("==== Não há saldo suficiente para sacar. ====")

    else:
        saldos = saldos - saque
        print(f"Saque de {saque} realizado.")
        return saldos

def ver_saldo(saldos):
        print(f"Saldo atual R$ {saldos}")

saldos = 0.0

while True:
    opcao = exibir_menu()
    if opcao == "0":
        print("==== Programa encerrado. ====")
        break

    if opcao not in ["1", "2", "3", "0"]:
        print("==== Opção inválida. Tente novamente. ====")
        continue

    if opcao == "1":
        saldos = depositar(saldos)

    if opcao == "2":
        saldos = sacar(saldos)

    if opcao == "3":
        ver_saldo(saldos)