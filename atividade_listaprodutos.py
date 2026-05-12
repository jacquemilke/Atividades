produtos = ["Camiseta", "Calça", "Par de meias", "Boné", "Touca"]
precos = [40.00, 80.00, 15.00, 20.00, 20.00]
quantidades = [2, 1, 2, 1, 1]
subtotais = []

for indice, produto in enumerate(produtos):
    preco = precos[indice]
    quantidade = quantidades[indice]
    subtotal = quantidade * preco
    subtotais.append(subtotal)

    mensagem = f"""
    --------------------
    Produto: {produto}
    Quantidade: {quantidade}
    Valor Unitário: {preco}
    Subtotal: {subtotal}
    """

    print(mensagem)

print(f"O total da compra deu: R${sum(subtotais)}")