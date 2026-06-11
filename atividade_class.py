class Aluno:
    def __init__(self, nome: str, nota: float):
        self.nome = nome
        self.nota = nota

    def exibir(self):
        print(f"O aluno {self.nome} tirou a nota: {self.nota}")

    def situacao(self):
        if self.nota >= 6:
            print(f"Aluno {self.nome} está aprovado.")
        
        else:
            print(f"Aluno {self.nome} está reprovado.")

def exibir_menu():
    print (f"""\n
    ====== CADASTRO ALUNO ======
    
    1 - Cadastrar Aluno
    2 - Exibir Aluno
    0 - Sair

    ==================
    """)

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    aluno = Aluno(nome, nota)
    alunos.append(aluno)

def exibir_alunos():
    if not alunos:
        print("Não há alunos cadastrados.")
        return
        
    for aluno in alunos:
        aluno.exibir()
        aluno.situacao()

alunos = []

while True:
    exibir_menu()
    opcao = input("Escolha uma opção. ")
   
    if opcao == "0":
        break

    elif opcao == "1":
        cadastrar_aluno()
    
    elif opcao == "2":
        exibir_alunos()
    
    else:
        print("Opção inválida.")