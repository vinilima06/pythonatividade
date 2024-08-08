# Solicita o peso e a altura do usuário
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Classifica o IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"
elif 25 <= imc < 29.9:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

# Exibe o IMC e a classificação correspondente
print(f"Seu IMC é {imc:.2f}. Você está classificado como: {classificacao}.")
