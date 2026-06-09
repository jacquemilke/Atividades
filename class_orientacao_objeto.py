"""
#A ideia da POO: manter tudo junto, num só lugar, tudo o que pertence à mesma coisa.

#Classe: o molde, a receita, a ficha em branco. Ela defina quais propriedads algo vai ter, mas ainda não é a coisa em si,

#Objeto: cada coisa criada a partir do molde. Tem as mesmas propriedades da classe, só que com valores próprios.

class Produto: #cria o molde chamado produto
    def __init__(self, nome, preco, qtd): #_init_ roda sozinho quando nasce um produto novo, é onde a ficha é preenchida.
        self.nome = nome #guarda o valor recebido dentro deste produto. "self" o próprio objeto falando de si mesmo.
        self.preco = preco
        self.qtd = qtd
    
    def mostrar(self):
        print(f"{self.nome}: R$ {self.preco}")



produtos = []

produtos.append(
    Produto("Arroz", 25.90, 10)
)

"""

class Produto:
    def __init__(self, nome: str, preco: float, qtd: int):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
    
    def exibir(self):
        print(f"Produto: {self.nome} | Preço: {self.preco} | Quantidade: {self.qtd}")

#primeira forma de fazer
produto_1 = Produto(nome="Arroz",
                    preco=7.0,
                    qtd=10)

#segunda forma de fazer
produto_2 = Produto("Feijão", 10.0, 15)

produto_1.exibir()
