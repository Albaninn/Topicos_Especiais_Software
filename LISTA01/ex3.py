print("Insira os valores reuisitados: ")

valor1 = float(input("Digite o valor 1: "))
valor2 = float(input("Digite o valor 2: "))

soma = valor1 + valor2
print(soma)
sub = valor1 - valor2
print(sub)
mult = valor1 * valor2
print(mult)
if valor2 == 0:
   print("Não é possivel dividir por 0")
else:
    div = valor1 / valor2
    print(div)