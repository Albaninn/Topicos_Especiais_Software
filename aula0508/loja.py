DESCONTO = 15
nome = input("Digite o nome do produto: ")
preço = float(input("Digite o preço do produto: "))
quant = int(input("Quantas unidades esta levando: "))

bruto = preço * quant
desconto = (bruto/100) * DESCONTO
final = bruto - desconto

print(f"O valor total dos {quant} {nome}(s) é de R${bruto},\nmas com o desconto de R${desconto} a compra ficou em R${final}")