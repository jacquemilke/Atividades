class Produto:
    def __init__(self, nome: str, preco: float, qtd: int):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
    
    def exibir(self):
        print(f"Produto: {self.nome} | Preço: {self.preco} | Quantidade: {self.qtd}")


def exibir_menu():
    print (f"""\n
    ====== MENU ======
    
    1 - Cadastrar Produto
    2 - Exibir Produto
    0 - Sair

    ==================
    """)

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    qtd = int(input("Digite a quantidade do produto: "))
    produto = Produto(nome, preco, qtd)
    produtos.append(produto)

def exibir_produtos():
    if not produtos:
        print("Não há produtos cadastrados.")
        return
        
    for produto in produtos:
        produto.exibir()

produtos = []

while True:
    exibir_menu()
    opcao = input("Escolha uma opção. ")
   
    if opcao == "0":
        break

    elif opcao == "1":
        cadastrar_produto()
    
    elif opcao == "2":
        exibir_produtos()
    
    else:
        print("Opção inválida.")