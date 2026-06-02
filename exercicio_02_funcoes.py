def exibir_menu():
    print (f"""\n
    ====== MENU ======
    1 - Celsius -> Fahrenheit
    2 - Reais -> Dólar
    3 - Horas -> Minutos
    0 - Sair
    ====== ==== ======
    """)
    
    opcao = input("Escolha uma opção: ")
    return opcao

def celsius_fahrenheit():
    valor = float(input("Digite um valor em celsius para converter: "))
    resultado = valor * 1.8 + 32
    print(f"A conversão de Celsius para Fahrenheit é: {round(resultado, 2)}")

def reais_dolar():
    valor = float(input("Digite um valor em dólar para converter: "))
    resultado = valor / 5
    print(f"A conversão de Reais para Dólar é: U$ {resultado}")

def horas_minutos():
    valor = float(input("Digite a quantidade de horas para converter: "))
    resultado = valor * 60
    print(f"A conversão de Horas para Minutos é: {resultado}")


while True:
    opcao = exibir_menu()
    if opcao == "0":
        print("Programa encerrado.")
        break

    if opcao not in ["1", "2", "3", "4", "0"]:
        print("Opção inválida. Tente novamente.")
        continue

    if opcao == "1": celsius_fahrenheit()
    
    elif opcao == "2": reais_dolar()

    elif opcao == "3": horas_minutos()