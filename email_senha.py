# Email e senha cadastrados antecipadamente
email_cadastrado = "esdrasfchiarelli@gmail.com"
senha_cadastrada = "72b95fky"

# Solicita ao usuário o email e a senha
while True:
    email_usuario = input("Digite seu email: ")
    senha_usuario = input("Digite sua senha: ")

    # Verifica se o email e a senha do usuário coincidem com os cadastrados antecipadamente
    if email_usuario == email_cadastrado and senha_usuario == senha_cadastrada:
        print("Login bem-sucedido!")
        break  # Sai do loop se o login for bem-sucedido
    else:
        print("Email ou senha incorretos. Tente novamente.")