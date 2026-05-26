#loja automotiva. Vendas de produtos. Serviços. usário entra com pedido de serviço ou produto. Mostrar a lista de produto ou serviço. Listas com nomes dos produtos e outra lista com nomes dos produtos. 

produtos = ["Cera", "Pneu", "Óleo"]
servicos = ["Troca de óleo", "Troca filtro", "Trocar bateria"]
valor_produtos = [20.50, 250.00, 100.40]
valor_servicos = [50.00, 85.60, 185.90]
cod_produto = [2]


print(f"""
      +--------------------------------------------+
      |         BEM - VINDO A AUTO CENTER          |
      +--------------------------------------------+
       
      Digite 1 para "Produtos"
      Digite 2 para "Serviços"
          
      +--------------------------------------------+
    """)

usuario = input("")

if usuario == "1":
    for indice, produto in enumerate(produtos):
        valor_produto = valor_produtos [indice]
        print(f"{produto} custa R$ {valor_produto}")


elif usuario == "2":
    for indice, servico in enumerate(servicos):
        valor_servico = valor_servicos [indice]
        print(f"{servico} custa R$ {valor_servico}")

else:
    print("Valor incorreto. Digite novamente.")

cod_produto = int(input("Digite o código escolhido: "))



print(f"""
      +--------------------------------------------+
      |                CUPOM FISCAL                |
      +--------------------------------------------+
      Item comprado: R$
      Desconto: R$
      O valor total: R$:
          
      +--------------------------------------------+
    """)