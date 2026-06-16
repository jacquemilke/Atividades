class Aluno:
    def __init__(self, nome: str, notas: list):
        self.nome = nome
        self.notas = notas

    def exibir(self):
        print(f"Nome: {self.nome}")
        if not self.notas:
            print("Não possui notas lançadas.")
            return

        for ordem_nota, nota in enumerate(self.notas, 1):
            print(f"Nota n.º {ordem_nota}: {nota}")

    def situacao(self):
        self.notas
        if not self.notas:
            print("Não foi possível ver a média pois não há notas lançadas.")
            return

        media = sum(self.notas) / len(self.notas)

        if media >= 6:
            print(f"Média: {media}. Aluno aprovado.")
        else:
            print(f"Média: {media}. Aluno reprovado.")

def exibir_menu():
    print (f"""\n
    ====== DIÁRIO DE CLASSE ======
    
    1 - Cadastrar aluno
    2 - Lançar notas
    3 - Ver situação do aluno
    4 - Listar alunos
    0 - Sair

    ==================
    """)

#opção 1
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    aluno = Aluno(nome, [])
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso.")

#opção 2
def lancar_nota():
    codigo_aluno = int(input("Digite o código do aluno: ")) - 1
    aluno = alunos[codigo_aluno]
    nota = float(input("Digite a nota para ser lançado: "))
    aluno.notas.append(nota)
    print(f"Nota {nota} lançada para o aluno {aluno.nome}")
    

#opção 3
def situacao():
    codigo_aluno = int(input("Digite o código do aluno: ")) - 1
    aluno = alunos[codigo_aluno]
    aluno.situacao()

#opção 4
def listar_alunos():
    if not alunos:
        print("Não há alunos cadastrados.")
        return
        
    for codigo_aluno, aluno in enumerate(alunos, 1):
        print(f"Código aluno: {codigo_aluno}")
        aluno.exibir()

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