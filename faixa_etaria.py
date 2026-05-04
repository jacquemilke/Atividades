idade = int(input ("digite a sua idade"))

if idade <= 12: 
    print(" voce ainda é criança")

elif idade > 12 and idade <= 16:
    print("voce é jovem")

elif idade > 16 and idade < 60:
    print("voce é adulto")

else:
    print("voce é idoso")
