DESCONTO_PADRAO = 0.105

acervo = []

def validar_float(mensagem):
    while True:
        texto = input(mensagem).strip().replace(",",".")
        try:
            valor = float(texto)
            return valor
        except ValueError:
            print("Entrada invalida. Digite um numero, use virgula ou ponto.")

def validar_int(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto.isdigit() or (texto.startswith("-") and texto[1:].isdigit()):
            return int(texto)
        print("Entrada invalida. Digite um numero inteiro.")

def pausar():
    input("\nPressione ENTER para continuar...")

def cadastrar_livro():
    print("\n--- Cadastro de Livro ---")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    preco = validar_float("Preço (R$): ")
    estoque = validar_int("Quantidade em estoque: ")

    if not isinstance(preco, float):
        print("Erro interno: preço não é float")
        return
    if not isinstance(estoque, int):
        print("Erro interno: estoque nao é int")
        return
    
    livro = {
        "titulo": titulo,
        "autor": autor,
        "preco": preco,
        "estoque": estoque
    }

    acervo.append(livro)
    print(f"\nLivro '{titulo}' cadastrado com sucesso! Total no acervo: {len(acervo)}")

def listar_livros():
    if not acervo:
        print("Nenhum livro cadastrado no momento.")
        return
    print("\nLista de livros")
    for i, livro in enumerate(acervo):
        print(
            f"{i} Titulo: {livro['titulo']} Autor: {livro['autor']} "
            f"Preço: R${livro['preco']} Estoque: {livro['estoque']} "
        )

def vender_livro():
    if not acervo:
        print("Nenhum livro cadastrado para venda.")
        return
    
    listar_livros()
    indice = validar_int("\nDigite o indice do livro que deseja vender: ")

    if indice < 0 or indice >= len(acervo):
        print("Indice inexistente")
        return
    
    livro = acervo[indice]
    print(
        f"Selecionado {livro['titulo']} de {livro['autor']} "
        f"Preço unitario R${livro['preco']}, estoque atual {livro['estoque']} "
    )

    if livro["estoque"] <= 0:
        print("Estoque esgotado")
        return
    
    quantidade = validar_int("Quantidade a vender: ")
    if quantidade <= 0:
        print("Quantidade deve ser positiva")
        return
    if quantidade > livro["estoque"]:
        print(f"Quantidade solicitada maior que o estoque. Disponivel {livro['estoque']}.")
        return
    
    valor_bruto = livro["preco"] * quantidade

    if valor_bruto > 100:
        valor_desconto = valor_bruto * DESCONTO_PADRAO
    else:
        valor_desconto = 0.0
    
    valor_liquido = valor_bruto - valor_desconto

    livro["estoque"] -= quantidade

    mostrar_resumo(livro, quantidade, valor_bruto, valor_desconto, valor_liquido)

def mostrar_resumo(livro, qtd, bruto, desconto, liquido):
    