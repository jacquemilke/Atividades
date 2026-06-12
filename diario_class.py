class Aluno:
    def __init__(self, nome, notas=[]):
        self.nome = nome
        self.notas = notas

    def exibir(self):
        print(f"Aluno: {self.nome}")
        if self.notas:
            for ordem_nota, nota in enumerate(self.notas, 1):
                print(f"Nota número {ordem_nota}: {nota}")

    def situacao(self):
        if self.notas:

            print(f"Aluno {self.nome} está aprovado.")
        
        else:
            print(f"Aluno {self.nome} está reprovado.")

def exibir_menu():
    print (f"""\n
    ====== DIÁRIO DE CLASSE ======
    
    1 - Cadastrar Aluno
    2 - Lançar Notas
    3 - Ver situação do Aluno
    4 - Listar Alunos
    0 - Sair

    ==================
    """)

#opção 1
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    aluno = Aluno(nome)
    alunos.append(alunos)
    print(f"Aluno {nome} cadastrado com sucesso.")

#opção 2
def lancar_nota():
    indice = int(input("Digite a nota do aluno: "))
    alunos = alunos[indice]
    nota = float(input("Digite a nota para ser lançado: "))
    aluno.notas.append(nota)
    print(f"Nota {nota} lançada para o aluno {aluno.nome}")
    

#opção 3
def situacao():
    nome = input("Digite o nome do aluno: ")

    if self.nota >= 6:
        print(f"Aluno {self.nome} está aprovado.")
        
    else:
        print(f"Aluno {self.nome} está reprovado.")

#opção 4
def listar_alunos():
    if not alunos:
        print("Não há alunos cadastrados.")
        return
        
    for aluno in alunos:
        alunos.exibir()
        alunos.situacao()

alunos = []

while True:
    exibir_menu()
    opcao = input("Escolha uma opção. ")
   
    if opcao == "0":
        break

    elif opcao == "1":
        cadastrar_aluno()
    
    elif opcao == "2":
        lancar_nota()

    elif opcao == "3":
        situacao()

    elif opcao == "4":
        listar_alunos()

    else:
        print("Opção inválida.")