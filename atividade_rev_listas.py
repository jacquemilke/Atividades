#crie uma lista vazia chamada compras. Adicione 3 itens nela usando o append().

compras = []

compras.append("arroz")
compras.append("feijão")
compras.append("ovos")
print(compras)

compras.remove("feijão")
print(compras)
print(len(compras))


#crie uma lista com vários números e salve ela uma variável de números. Faça a soma de todos os números e ao final exiba uma mensagem dizendo o total dessa soma.

numeros = [10, 20, 20]
total = sum(numeros)
print(total)


#Agora coloque uma condicional, se o tamanho da lista for maior ou igual que 4 elementos, você soma, senão, diz que precisa inserir mais elementos.

numeros = [10, 20, 20]
Quantidade = len(numeros)

if Quantidade >= 4:
    total = sum(numeros)
    
else:
    print("Insira mais números")
