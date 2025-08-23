# Etapa 1: Constantes (sem alteração)
DESCONTO_PADRAO = 0.105
VALOR_MINIMO_DESCONTO = 100.00

# Etapa 2: Estrutura de dados para o estoque de bebidas
estoque_bebidas = []

# Etapa 3: Funções de validação e utilitárias (sem alteração)

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

# Etapa 4: Cadastro de bebidas (sem alteração)
def cadastrar_bebida():
    """Função para cadastrar uma nova bebida no estoque."""
    print("\n--- Cadastro de Bebida ---")
    nome = input("Nome da bebida: ").strip()
    marca = input("Marca: ").strip()
    tipo = input("Tipo (ex: Cerveja, Vinho, Refrigerante): ").strip()
    preco = validar_float("Preço (R$): ")
    volume_ml = validar_int("Volume (ml): ")
    estoque = validar_int("Quantidade em estoque: ")

    bebida = {
        "nome": nome,
        "marca": marca,
        "tipo": tipo,
        "preco": preco,
        "volume_ml": volume_ml,
        "estoque": estoque
    }
    
    estoque_bebidas.append(bebida)
    print(f"\nBebida '{nome}' cadastrada com sucesso!")
    pausar()

# Etapa 5: Listagem de bebidas (Refatorado para começar em 1)
def listar_bebidas():
    """Função para exibir todas as bebidas cadastradas no estoque."""
    print("\n--- Estoque de Bebidas ---")
    if not estoque_bebidas:
        print("Nenhuma bebida cadastrada no momento.")
    else:
        # MODIFICAÇÃO: Usamos start=1 para a lista começar em 1 para o usuário.
        for i, bebida in enumerate(estoque_bebidas, start=1):
            print(f"[{i}] - Nome: {bebida['nome']} ({bebida['marca']})")
            print(f"      Tipo: {bebida['tipo']}")
            print(f"      Volume: {bebida['volume_ml']}ml")
            print(f"      Preço: R$ {bebida['preco']:.2f}")
            print(f"      Estoque: {bebida['estoque']} unidades")
            print("-" * 25)
    pausar()

# Etapa 7: Resumo da venda (sem alteração na lógica interna)
def resumo_venda(carrinho):
    """Exibe o resumo da compra, calcula descontos e atualiza o estoque."""
    print("\n--- Resumo da Venda ---")
    subtotal = 0
    
    for item in carrinho:
        total_item = item['preco_unitario'] * item['quantidade']
        print(f"{item['quantidade']}x '{item['nome']}' (R$ {item['preco_unitario']:.2f}) = R$ {total_item:.2f}")
        subtotal += total_item
        
        for bebida_estoque in estoque_bebidas:
            if bebida_estoque['nome'] == item['nome']:
                bebida_estoque['estoque'] -= item['quantidade']
                break

    print("\n------------------------------")
    print(f"Subtotal: R$ {subtotal:.2f}")

    if subtotal > VALOR_MINIMO_DESCONTO:
        valor_desconto = subtotal * DESCONTO_PADRAO
        total_final = subtotal - valor_desconto
        print(f"Desconto ({DESCONTO_PADRAO * 100:.1f}%): R$ {valor_desconto:.2f}")
    else:
        total_final = subtotal
        print("Compras acima de R$ 100.00 recebem desconto.")

    print(f"TOTAL A PAGAR: R$ {total_final:.2f}")
    print("------------------------------")
    print("\nVenda finalizada com sucesso!")
    pausar()

# Etapa 6: Venda de bebidas (Refatorado para começar em 1)
def vender_bebidas():
    """Função para realizar a venda de uma ou mais bebidas."""
    print("\n--- Venda de Bebidas ---")
    if not estoque_bebidas:
        print("Nenhuma bebida cadastrada para vender.")
        pausar()
        return

    print("Bebidas disponíveis:")
    # MODIFICAÇÃO: Usamos start=1 para a lista começar em 1 para o usuário.
    for i, bebida in enumerate(estoque_bebidas, start=1):
        print(f"[{i}] {bebida['nome']} - Estoque: {bebida['estoque']} - R$ {bebida['preco']:.2f}")
    
    carrinho = []
    while True:
        while True:
            indice_str = input("\nDigite o número da bebida que deseja comprar (ou pressione ENTER para finalizar): ").strip()
            if indice_str == "":
                break
            try:
                # O número que o usuário digita (1, 2, 3...)
                indice_usuario = int(indice_str)
                # MODIFICAÇÃO: Validamos se o número está no intervalo de 1 até o total de bebidas.
                if 1 <= indice_usuario <= len(estoque_bebidas):
                    break
                else:
                    print("Número de bebida inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
        
        if indice_str == "":
            break

        # MODIFICAÇÃO: Convertemos o índice do usuário (1-based) para o índice da lista (0-based)
        indice_lista = indice_usuario - 1
        bebida_selecionada = estoque_bebidas[indice_lista]
        
        if bebida_selecionada['estoque'] == 0:
            print(f"Desculpe, a bebida '{bebida_selecionada['nome']}' está fora de estoque.")
            continue 

        while True:
            quantidade = validar_int(f"Digite a quantidade de '{bebida_selecionada['nome']}' (disponível: {bebida_selecionada['estoque']}): ")
            if 0 < quantidade <= bebida_selecionada['estoque']:
                break
            else:
                print(f"Quantidade inválida. O valor deve ser entre 1 e {bebida_selecionada['estoque']}.")
        
        carrinho.append({
            "nome": bebida_selecionada['nome'],
            "quantidade": quantidade,
            "preco_unitario": bebida_selecionada['preco']
        })
        print(f"{quantidade}x '{bebida_selecionada['nome']}' adicionado(s) ao carrinho.")

        continuar = input("Deseja adicionar outra bebida? [S/N]: ").strip().upper()
        if continuar != 'S':
            break

    if carrinho:
        resumo_venda(carrinho)
    else:
        print("Nenhum item no carrinho. Venda cancelada.")
        pausar()

# Etapa 8: Menu principal (sem alteração)
def menu_principal():
    """Exibe o menu principal e gerencia a navegação do usuário."""
    while True:
        print("\n--- Sistema da Loja de Bebidas ---")
        print("1 - Cadastrar Bebida")
        print("2 - Listar Bebidas")
        print("3 - Vender Bebidas")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            cadastrar_bebida()
        elif opcao == '2':
            listar_bebidas()
        elif opcao == '3':
            vender_bebidas()
        elif opcao == '4':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")
            pausar()

# Etapa 9: Execução do programa
if __name__ == "__main__":
    menu_principal()