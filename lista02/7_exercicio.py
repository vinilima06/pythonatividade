# Solicita que o usuário insira um dia da semana
dia_semana = input("Digite um dia da semana (ex: segunda, terça, etc.): ").strip().lower()

# Usa a estrutura match para verificar se é dia útil ou fim de semana
match dia_semana:
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print(f"{dia_semana.capitalize()} é um dia útil.")
    case "sábado" | "sabado" | "domingo":
        print(f"{dia_semana.capitalize()} é fim de semana.")
    case _:
        print("Dia inválido. Por favor, insira um dia da semana válido.")