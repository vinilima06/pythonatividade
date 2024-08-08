# Define as alturas das duas pessoas (em metros)
altura_pessoa1 = float(input("Digite a altura da primeira pessoa (em metros): "))
altura_pessoa2 = float(input("Digite a altura da segunda pessoa (em metros): "))

# Verifica qual das pessoas é mais alta e exibe a mensagem correspondente
if altura_pessoa1 > altura_pessoa2:
    print("A primeira pessoa é mais alta.")
elif altura_pessoa2 > altura_pessoa1:
    print("A segunda pessoa é mais alta.")
else:
    print("Ambas as pessoas têm a mesma altura.")