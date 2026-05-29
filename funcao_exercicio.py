"""
Uma função é um bloco de código que realiza uma tarefa específica.

define uma vez -> chama quando quiser -> reaproveita sempre

#sintaxe
def nome_da_funcao(parametro):
    #bloco de código
    #instruções usando os parâmetros
    return resultado #opcional

#exemplo
def somar(a, b):
    resultado = a + b
    return resultado

#chamando a função
soma = somar(3, 5) #soma recebe 8
print(soma)

"""
def somar(numero_1, numero_2): print(f"A soma de {numero_1} + {numero_2} é de: {numero_1 + numero_2}")

def subtrair(numero_1, numero_2): print(f"A subtração de {numero_1} e {numero_2} é de: {umero_1 - numero_2}")

def multiplicar(numero_1, numero_2): print(f"A multipicação de {numero_1} e {numero_2} é de: {numero_1 * numero_2}")

def dividir(numero_1, numero_2):
    if numero_2 == 0: print("Não é possível dividir por zero")
        
    else: print(f"A divisão de {numero_1} e {numero_2} é de: {round(numero_1 / numero_2, 2)}")

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

    if escolha == "1": somar(numero_1, numero_2)
    
    elif escolha == "2": subtrair(numero_1, numero_2)
        
    elif escolha == "3": multiplicar(numero_1, numero_2)

    elif escolha == "4": dividir(numero_1, numero_2)   

#-------------------------------------#

def Calcular_media(notas):
    """
    Calcula  a média de uma lista de notas.
    :param notas: Lista de números (ex: [7, 8.5, 9])
    :return: Números float com a média
    """
    if not notas: return 0
    return sum(notas) / len(notas)


