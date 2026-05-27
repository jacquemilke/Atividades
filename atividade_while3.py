# Listas de produtos e preços
produtos = ["Pneu", "Bateria", "Óleo", "Palheta"]
precos_produtos = [400.00, 350.00, 50.00, 30.00]
 
# Listas de serviços e preços
servicos = ["Alinhamento", "Revisão", "Lavagem"]
precos_servicos = [100.00, 150.00, 50.00]
 
# Pergunta ao cliente
print("Você deseja ver nossos Produtos ou Serviços?")
escolha = input()
 
# Exibe produtos
if escolha == "Produto":
    print("Produtos disponíveis:")
    i = 0
    while i < len(produtos):
        print(str(i) + " - " + produtos[i] + " - R$ " + str(precos_produtos[i]))
        i = i + 1
    categoria = "produto"
 
# Exibe serviços
elif escolha == "Serviço":
    print("Serviços disponíveis:")
    i = 0
    while i < len(servicos):
        print(str(i) + " - " + servicos[i] + " - R$ " + str(precos_servicos[i]))
        i = i + 1
    categoria = "serviço"
 
# Opção inválida
else:
    print("Opção inválida.")
    exit()
 
# Pede para o cliente escolher um item
print("Digite o número do item que deseja comprar:")
indice_item = int(input())
 
# Verifica qual item foi escolhido
if categoria == "produto":
    if indice_item >= 0 and indice_item < len(produtos):
        nome_item = produtos[indice_item]
        preco_original = precos_produtos[indice_item]
    else:
        print("Número inválido.")
        exit()
else:
    if indice_item >= 0 and indice_item < len(servicos):
        nome_item = servicos[indice_item]
        preco_original = precos_servicos[indice_item]
    else:
        print("Número inválido.")
        exit()
 
# Aplica desconto se for maior que 300
if preco_original > 300:
    preco_final = preco_original - (preco_original * 0.10)
else:
    preco_final = preco_original
 
# Mostra o cupom fiscal
print("--------- CUPOM FISCAL ---------")
print("Item comprado: " + nome_item)
print("Valor a pagar: R$ " + str(preco_final))
print("--------------------------------")