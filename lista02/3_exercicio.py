# Solicita o nome de usuário e a senha do usuário
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

# Verifica se o nome de usuário é "admin" e a senha é "1234"
if usuario == "admin" and senha == "1234":
    print("Login bem-sucedido! Bem-vindo, admin.")
else:
    print("Erro de login! Nome de usuário ou senha incorretos.")
    