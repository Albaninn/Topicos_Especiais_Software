# Etapa 1: Constante de desconto
DESCONTO_PADRAO = 0.105
VALOR_MINIMO_DESCONTO = 100.00 # Nova constante para clareza

# Etapa 2: Estrutura de dados para o acervo
acervo = []

# Etapa 3: Funções de validação e utilitárias

def validar_float(mensagem):
    """Solicita um número de ponto flutuante (float) ao usuário, tratando erros."""
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(texto)
            if valor >= 0:
                return valor
            else:
                print("Entrada inválida. Digite um número positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número, usando vírgula ou ponto para casas decimais.")

def validar_int(mensagem):
    """Solicita um número inteiro (int) ao usuário, tratando erros."""
    while True:
        texto = input(mensagem).strip()
        try:
            valor = int(texto)
            if valor >= 0:
                return valor
            else:
                print("Entrada inválida. Digite um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def pausar():
    """Pausa a execução do programa até que o usuário pressione ENTER."""
    input("\nPressione ENTER para continuar...")

# Etapa 4: Cadastro de livros
def cadastrar_livro():
    """Função para cadastrar um novo livro no acervo."""
    print("\n--- Cadastro de Livro ---")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    preco = validar_float("Preço (R$): ")
    estoque = validar_int("Quantidade em estoque: ")

    # As verificações abaixo foram removidas pois as funções de validação já garantem o tipo correto
    livro = {
        "titulo": titulo,
        "autor": autor,
        "preco": preco,
        "estoque": estoque
    }
    
    acervo.append(livro)
    print(f"\nLivro '{titulo}' cadastrado com sucesso!")
    pausar()

# Etapa 5: Listagem de livros
def listar_livros():
    """Função para exibir todos os livros cadastrados no acervo."""
    print("\n--- Acervo de Livros ---")
    if not acervo:
        print("Nenhum livro cadastrado no momento.")
    else:
        for i, livro in enumerate(acervo):
            print(f"[{i}] - Título: {livro['titulo']}")
            print(f"    Autor: {livro['autor']}")
            print(f"    Preço: R$ {livro['preco']:.2f}")
            print(f"    Estoque: {livro['estoque']} unidades")
            print("-" * 25)
    pausar()

# Etapa 7: Resumo da venda
def resumo_venda(carrinho):
    """Exibe o resumo da compra, calcula descontos condicionalmente e atualiza o estoque."""
    print("\n--- Resumo da Venda ---")
    subtotal = 0
    
    for item in carrinho:
        total_item = item['preco_unitario'] * item['quantidade']
        print(f"{item['quantidade']}x '{item['titulo']}' (R$ {item['preco_unitario']:.2f}) = R$ {total_item:.2f}")
        subtotal += total_item
        
        # Atualiza o estoque no acervo principal
        for livro_acervo in acervo:
            if livro_acervo['titulo'] == item['titulo']:
                livro_acervo['estoque'] -= item['quantidade']
                break

    print("\n------------------------------")
    print(f"Subtotal: R$ {subtotal:.2f}")

    # --- LÓGICA DO DESCONTO CONDICIONAL ---
    # Verifica se o subtotal é maior que o valor mínimo para desconto
    if subtotal > VALOR_MINIMO_DESCONTO:
        valor_desconto = subtotal * DESCONTO_PADRAO
        total_final = subtotal - valor_desconto
        print(f"Desconto ({DESCONTO_PADRAO * 100:.1f}%): R$ {valor_desconto:.2f}")
    else:
        # Se for menor ou igual a 100, não há desconto
        total_final = subtotal
        print("Compras acima de R$ 100.00 recebem desconto.")
    # --- FIM DA LÓGICA DO DESCONTO ---

    print(f"TOTAL A PAGAR: R$ {total_final:.2f}")
    print("------------------------------")
    print("\nVenda finalizada com sucesso!")
    pausar()

# Etapa 6: Venda de livros
def vender_livros():
    """Função para realizar a venda de um ou mais livros."""
    print("\n--- Venda de Livros ---")
    if not acervo:
        print("Nenhum livro cadastrado para vender.")
        pausar()
        return

    # Exibe a lista de livros de forma simples, sem pausar
    print("Livros disponíveis:")
    for i, livro in enumerate(acervo):
        print(f"[{i}] {livro['titulo']} - Estoque: {livro['estoque']} - R$ {livro['preco']:.2f}")
    
    carrinho = []
    while True:
        while True:
            # Tratamento para entrada vazia para finalizar a compra
            indice_str = input("\nDigite o número do livro que deseja comprar (ou pressione ENTER para finalizar): ").strip()
            if indice_str == "":
                break
            try:
                indice_livro = int(indice_str)
                if 0 <= indice_livro < len(acervo):
                    break
                else:
                    print("Número de livro inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
        
        if indice_str == "":
            break
            
        livro_selecionado = acervo[indice_livro]
        
        if livro_selecionado['estoque'] == 0:
            print(f"Desculpe, o livro '{livro_selecionado['titulo']}' está fora de estoque.")
            continue 

        while True:
            quantidade = validar_int(f"Digite a quantidade de '{livro_selecionado['titulo']}' (disponível: {livro_selecionado['estoque']}): ")
            if 0 < quantidade <= livro_selecionado['estoque']:
                break
            else:
                print(f"Quantidade inválida. O valor deve ser entre 1 e {livro_selecionado['estoque']}.")
        
        carrinho.append({
            "titulo": livro_selecionado['titulo'],
            "quantidade": quantidade,
            "preco_unitario": livro_selecionado['preco']
        })
        print(f"{quantidade}x '{livro_selecionado['titulo']}' adicionado(s) ao carrinho.")

        continuar = input("Deseja adicionar outro livro? [S/N]: ").strip().upper()
        if continuar != 'S':
            break

    if carrinho:
        resumo_venda(carrinho)
    else:
        print("Nenhum item no carrinho. Venda cancelada.")
        pausar()

# Etapa 8: Menu principal
def menu_principal():
    """Exibe o menu principal e gerencia a navegação do usuário."""
    while True:
        print("\n--- Sistema de Livraria ---")
        print("1 - Cadastrar Livro")
        print("2 - Listar Livros")
        print("3 - Vender Livros")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            vender_livros()
        elif opcao == '4':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")
            pausar()

# Etapa 9: Execução do programa
if __name__ == "__main__":
    menu_principal()