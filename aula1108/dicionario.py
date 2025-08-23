id = int(input("Digite quanto produtos serão cadastrados: "))
produtos = []
precos_por_produto = {}
for i in range(id):
    nome = input(f"Digite o nome do produto {i+1}: ")
    preco = float(input(f"Digite o preço do produto {i+1}: "))
    produtos.append(nome)
    precos_por_produto[nome] = preco
print("\n--- Cadastro de Produtos ---")
for nome in produtos:
    preco = precos_por_produto[nome]
    print(f"Produto: {nome}, Preço: R$ {preco:.2f}")