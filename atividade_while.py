#peça o nome de usuário e senha, cada um com sua variável. Considere o usuário correto como "admin" e a senha como "1234".
#se ambos estiverem corretos, exiba "Acesso permitido"
#caso contrário, exiba "Usuário ou senha inválidos"

usuario_correto = "admin"
senha_correta = "1234"

usuario = ""
senha = ""

while usuario != usuario_correto or senha != senha_correta:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario != usuario_correto or senha != senha_correta:
        print("Usuário ou senha inválidos. Digite novamente: ")

else:
    print("Acesso permitido.")