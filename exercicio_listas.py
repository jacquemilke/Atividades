produtos = ["Fone de ouvido", "Celular", "Notebook", "Mouse", "Projetor"]
precos = [40.00, 80.00, 15.00, 20.00, 20.00]

print(f"O produto {produtos[0]} custa R$ {precos[0]}.")
produtos.remove(produtos[-1])
precos.remove(precos[-1])

total_precos = sum(precos)
print(f"O total deu R${total_precos}.")

if total_precos < 100:
    exit()

else:
    desconto = 0.95
    total_geral = total_precos * desconto
    descontoPercentual = (1 - desconto) * 100
    descontoPercentual = round(descontoPercentual,0)
    print(f"Sua compra deu R${total_precos}. Você ganhou {descontoPercentual}% de desconto. O total agora é R$ {total_geral}")    