class Produto:
    def __init__(self, nome, preco, setor):
        self.nome = nome
        self.preco = preco
        self.setor = setor

    def exibir(self):
        print(f"Nome: {self.nome} | Preço: {self.preco} | Setor: {self.setor}")

#opção 1
def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    setor = input("Digite o setor do produto: ")
    produto = Produto(nome, preco, setor)
    carrinho.append(produto)

#opção 2
def exibir_produtos_e_total():
    if not carrinho:
        print("Não há produtos cadastrados.")
        print("Total do carrinho: R$0.0")
        return

    total = 0

    for produto in carrinho:
        produto.exibir()
        total += produto.preco

    print(f"Total do carrinho: R$ {total}")

#opção 3
def filtrar_por_setor():
    setor = input("Setor para filtrar: ")

    for codigo_produto, produto in enumerate(carrinho, 1):
        if setor == produto.setor:
            print(f"Código produto: {codigo_produto}")
            produto.exibir()

def exibir_menu():
    print (f"""\n
    ====== CARRINHO DE COMPRAS ======
    
    1 - Cadastrar produto
    2 - Calcular total
    3 - Filtrar por setor
    0 - Sair

    =================================
    """)


carrinho = []

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
   
    if opcao == "0":
        break

    elif opcao == "1":
        cadastrar_produto()
    
    elif exibir_produtos_e_total == "2":
        listar_produtos()

    elif filtrar_por_setor == "3":
        situacao()

    else:
        print("Opção inválida.")