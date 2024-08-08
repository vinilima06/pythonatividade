# Solicita a nota do exame
nota = float(input("Digite a nota do exame: "))

# Usa um IF ternário para verificar se o aluno foi aprovado ou reprovado
resultado = "Aprovado" if nota >= 5 else "Reprovado"

# Exibe o resultado
print(f"Você foi {resultado}.")
