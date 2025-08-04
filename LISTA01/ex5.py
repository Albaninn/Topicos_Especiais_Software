idade = float(input("Digite sua idade: "))

if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolecente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")