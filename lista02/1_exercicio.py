nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

# Verifica se a idade é suficiente para votar
if idade >= 16:
    print(f"{nome}, você tem idade suficiente para votar!")
else:
    print(f"{nome}, você ainda não tem idade suficiente para votar.")