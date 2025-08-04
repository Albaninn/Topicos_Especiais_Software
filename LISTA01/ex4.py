print("Insira os valores requisitados: ")

peso = float(input("Digite seu peso (em Kg): "))
altura = float(input("Digite sua altura (em metros): "))

imc = peso/(altura*2)

print(imc)
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("normal")
elif imc < 30:
    print("sobrepeso")
else:
    print("obesidade")