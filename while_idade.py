#peça ao usuário uma idade entre 0 e 120. Enquanto for válida, continue pedindo.
idade = -1

while idade < 0 or idade > 120:
    idade = int(input("Digite uma idade válida (0 a 120). "))

    if idade < 0 or idade > 120:
        print("Idade inválida! Tente novamente.")

print(f"Obrigado! A idade digitada foi {idade}.")
        