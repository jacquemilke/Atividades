import random
numero_secreto = random.randint(1, 10)
palpite = 0
tentativas = 0

while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número (1 a 10): "))
    if palpite != numero_secreto:
        print(f"Errou! Tente novamente.\n")
    tentativas = tentativas + 1

if tentativas == 1:
    print(f"Acertou! Você tentou {tentativas} vez.")

else:
    print(f"Acertou! Você tentou {tentativas} vezes.")