valor = float(input("Digite o valor do pedido:"))

"""
Regra de negócio:
se a venda for até R$ 100: não tem desconto
se a venda for entre R$ 100,01 e R$ 299,99: 10% de desconto
se a venda for acima de R$ 300: 15% de desconto
"""

if valor <= 100:
    print(f"O valor da compra deu R${valor}.")
    exit()

    
elif valor > 100 and valor <= 299.99:
    desconto = 0.90
    
else:
    desconto = 0.85

total = valor * desconto
descontoPercentual = (1 - desconto) * 100
descontoPercentual = round(descontoPercentual,0)
#print("Valor total foi de: ", total, "e seu desconto foi de:", descontoPercentual, "%)")
print(f"Sua compra deu R${valor}. Você ganhou {descontoPercentual}% de desconto. O total agora é R$ {total}")