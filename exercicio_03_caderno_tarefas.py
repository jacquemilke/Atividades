def exibir_menu():
    print (f"""\n
    ====== MENU CADERNO DE TAREFAS ======
    1 - Adicionar
    2 - Listar
    3 - Remover
    0 - Sair
    ============ FIM DA LISTA ===========
    """)
    
    opcao = input("Escolha uma opção: ")
    return opcao

tarefas = []

def adicionar():
    add_tarefa = input("Digite a tarefa para ser adicionada: ")
    tarefas.append(add_tarefa)
    print(f"A tarefa {add_tarefa} foi adicionada ao seu carderno.")

def listar():
    if not tarefas:
        print("==== Não há tarefas para listar. ====")

    else:
        print(f"Essa é a sua lista de tarefas: ")
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1} - {tarefa}")
        

def remover():
    if not tarefas:
        print("==== Não há tarefas para remover. ====")
        
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1} - {tarefa}")

    else:
        remove_tarefa = int(input(f"Digite o número que deseja remover a tarefa: "))
        
        tarefas.pop(remove_tarefa -1)
        print("==== A tarefa foi removida. ====")

while True:
    opcao = exibir_menu()
    if opcao == "0":
        print("==== Programa encerrado. ====")
        break

    if opcao not in ["1", "2", "3", "0"]:
        print("==== Opção inválida. Tente novamente. ====")
        continue

    if opcao == "1": adicionar()

    if opcao == "2": listar()

    if opcao == "3": remover()