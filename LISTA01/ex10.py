'''10. Simulação de Compras
o Peça nome e preço de 3 produtos.
o Calcule o total, aplique desconto de 10% se o valor ultrapassar R$ 100 e mostre o valor final.'''


nome1 = input("Digite o nome do produto 1: ")
preço1 = int(input("Digite o preço do produto 1: "))
nome2 = input("Digite o nome do produto 2: ")
preço2 = int(input("Digite o preço do produto 2: "))
nome3 = input("Digite o nome do produto 3: ")
preço3 = int(input("Digite o preço do produto 3: "))

total = preço1 + preço2 + preço3


print ("\nSeu total foi de: R$", total)
if total > 100:
    desconto = (total/100) * 10
    total_real = total - desconto
    print ("Seu total com desconto foi de: R$", total_real)
