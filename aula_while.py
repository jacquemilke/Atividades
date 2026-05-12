#vamos aprender a "pular partes" de um loop, seja ele "for" ou "while"
#sintaxe:
for numero in range(1, 6):
    if numero == 3:
        continue
    print(numero)

#e se quisermos ignorar um conjunto de números
for numero in range(1, 6):
    if numero in [3, 4, 5]:
        continue
    print(numero)

