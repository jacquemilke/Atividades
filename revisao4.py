#peça o nome de usuário e senha, cada um com sua variável. Considere o usuário correto como "admin" e a senha como "1234".
#se ambos estiverem corretos, exiba "Acesso permitido"
#caso contrário, exiba "Usuário ou senha inválidos"

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

usuario_correto = "admin"
senha_correta = "1234"

if usuario == usuario_correto and senha == senha_correta:
    print("Acesso permitido.")
else:
    print("Usuário ou senha inválidos")