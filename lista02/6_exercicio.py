# Exibe o menu de opções
print("Menu de Opções de Comida:")
print("1: Pizza")
print("2: Hambúrguer")
print("3: Salada")

# Solicita que o usuário escolha uma opção
opcao = int(input("Escolha uma opção (1, 2 ou 3): "))

# Usa a estrutura match para exibir a comida selecionada
match opcao:
    case 1:
        print("Você escolheu Pizza.")
    case 2:
        print("Você escolheu Hambúrguer.")
    case 3:
        print("Você escolheu Salada.")
    case _:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")