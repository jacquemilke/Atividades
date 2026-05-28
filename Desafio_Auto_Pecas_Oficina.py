produtos = ["Pneu", "Bateria", "Óleo", "Palheta"]
precos_produtos = [400.00, 150.00, 50.00, 30.00]

servicos = ["Alinhamento", "Revisão", "Lavagem"]
precos_servicos = [500.00, 150.00, 50.00]

escolha_tipo = input("Você deseja ver nossos Produtos ou Serviços? ")

if escolha_tipo == "Produto":
    print("\nProdutos disponíveis:")
    for indice, produto in enumerate(produtos):
        preco_produto = precos_produtos [indice]
        print(f"{produto} custa - R$ {preco_produto}")

elif escolha_tipo == "Serviço":
    for indice, servico in enumerate(servicos):
        preco_servico = precos_servicos [indice]
        print(f"{servico} custa - R$ {preco_servico}")

else:
    print("Opção inválida")
    exit

codigo = int(input("Digite o número do item que deseja comprar: "))

if escolha_tipo == "Produto":
    nome_escolhido = produtos[codigo]
    preco_escolhido = precos_produtos[codigo]

elif escolha_tipo == "Serviço":
    nome_escolhido = servicos[codigo]
    preco_escolhido = precos_servicos[codigo]

if preco_escolhido >= 300:
    preco_escolhido = round(preco_escolhido * 0.90, 2)

mensagem = f"""
    +--------------------------------------------+
    |                 CUPOM FISCAL               |
    +--------------------------------------------+
    Produto: {nome_escolhido}
    Valor: R$ {preco_escolhido}
    
    """
    
print(mensagem)