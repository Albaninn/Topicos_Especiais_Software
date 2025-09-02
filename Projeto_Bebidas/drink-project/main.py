from desconto_padrao_da_loja import desconto_padrao_da_loja

# --- Constantes Globais ---
DESCONTO_PADRAO = 0.105
VALOR_MINIMO_DESCONTO = 100.00

# --- Variavel Globais ---
t = False

# --- Estrutura de Dados Principal ---
estoque_bebidas = []

# --- Funções de Validação e Utilitários ---
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

# --- Funções Relacionadas ao Cadastro (Conceito Cap. 8.7) ---
def _criar_dicionario_bebida(nome, marca, tipo, preco, volume_ml, estoque):
    """Cria e retorna um dicionário representando uma bebida."""
    return {
        "nome": nome,
        "marca": marca,
        "tipo": tipo,
        "preco": preco,
        "volume_ml": volume_ml,
        "estoque": estoque
    }

def cadastrar_bebida():
    """
    Coleta os dados de uma nova bebida e usa o desempacotamento de parâmetros
    para criar o registro. (Conceito Cap. 8.7)
    """
    print("\n--- Cadastro de Bebida ---")
    nome = input("Nome da bebida: ").strip()
    marca = input("Marca: ").strip()
    tipo = input("Tipo (ex: Cerveja, Vinho, Refrigerante): ").strip()
    preco = validar_float("Preço (R$): ")
    volume_ml = validar_int("Volume (ml): ")
    estoque_atual = validar_int("Quantidade em estoque: ")

    parametros_bebida = [nome, marca, tipo, preco, volume_ml, estoque_atual]
    
    # Desempacota a lista 'parametros_bebida' nos argumentos da função auxiliar
    bebida = _criar_dicionario_bebida(*parametros_bebida)
    
    estoque_bebidas.append(bebida)
    print(f"\nBebida '{nome}' cadastrada com sucesso!")
    pausar()

# --- Funções Relacionadas à Listagem (Conceito Cap. 8.8) ---
def listar_bebidas(*indices):
    """
    Exibe as bebidas. Se nenhum índice for passado, exibe todas.
    Caso contrário, exibe apenas as bebidas nos índices especificados. (Conceito Cap. 8.8)
    """
    print("\n--- Estoque de Bebidas ---")
    if not estoque_bebidas:
        print("Nenhuma bebida cadastrada no momento.")
        pausar()
        return

    if not indices:
        # Comportamento original: listar todas as bebidas.
        for i, bebida in enumerate(estoque_bebidas):
            print(f"[{i+1}] - Nome: {bebida['nome']} ({bebida['marca']})")
            print(f"      Preço: R$ {bebida['preco']:.2f} | Estoque: {bebida['estoque']} unidades")
            print("-" * 25)
    else:
        # Comportamento novo: listar apenas os índices especificados.
        for i in indices:
            if 0 <= i < len(estoque_bebidas):
                bebida = estoque_bebidas[i]
                print(f"[{i+1}] - Nome: {bebida['nome']} ({bebida['marca']})")
                print(f"      Preço: R$ {bebida['preco']:.2f} | Estoque: {bebida['estoque']} unidades")
                print("-" * 25)
            else:
                print(f"Código {i+1} é inválido e será ignorado.")
    pausar()

def resumo_venda(carrinho, desconto_padrao_da_loja):
    """
    Exibe o resumo da compra, calcula descontos usando uma função passada
    como parâmetro e atualiza o estoque. (Conceito Cap. 8.6)
    """
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
    
    # Usa a função de desconto que foi passada como parâmetro
    valor_desconto, mensagem_desconto = desconto_padrao_da_loja(subtotal)
    
    print(mensagem_desconto)
    total_final = subtotal - valor_desconto
    print(f"TOTAL A PAGAR: R$ {total_final:.2f}")
    print("------------------------------")
    print("\nVenda finalizada com sucesso!")
    pausar()

def vender_bebidas():
    """Função para realizar a venda de uma ou mais bebidas."""
    print("\n--- Venda de Bebidas ---")
    if not estoque_bebidas:
        print("Nenhuma bebida cadastrada para vender."); pausar(); return
    print("Bebidas disponíveis:")
    for i, bebida in enumerate(estoque_bebidas):
        print(f"[{i+1}] {bebida['nome']} - Estoque: {bebida['estoque']} - R$ {bebida['preco']:.2f}")
    carrinho = []
    while True:
        while True:
            indice_str = input("\nDigite o número da bebida (ou ENTER para finalizar): ").strip()
            if indice_str == "": break
            try:
                indice_usuario = int(indice_str)
                if 1 <= indice_usuario <= len(estoque_bebidas): break
                else: print("Número de bebida inválido.")
            except ValueError: print("Entrada inválida.")
        if indice_str == "": break
        indice_lista = indice_usuario - 1
        bebida_selecionada = estoque_bebidas[indice_lista]
        if bebida_selecionada['estoque'] == 0:
            print(f"Desculpe, '{bebida_selecionada['nome']}' está fora de estoque."); continue 
        while True:
            quantidade = validar_int(f"Quantidade de '{bebida_selecionada['nome']}' (disp: {bebida_selecionada['estoque']}): ")
            if 0 < quantidade <= bebida_selecionada['estoque']: break
            else: print(f"Quantidade inválida. Deve ser entre 1 e {bebida_selecionada['estoque']}.")
        carrinho.append({"nome": bebida_selecionada['nome'], "quantidade": quantidade, "preco_unitario": bebida_selecionada['preco']})
        print(f"{quantidade}x '{bebida_selecionada['nome']}' adicionado(s).")
        continuar = input("Adicionar outra bebida? [S/N]: ").strip().upper()
        if continuar != 'S': break
    if carrinho:
        resumo_venda(carrinho, desconto_padrao_da_loja)
    else:
        print("Nenhum item no carrinho. Venda cancelada."); pausar()

# --- Menus de Navegação ---
def submenu_listar_bebidas():
    """Gerencia as opções de listagem de bebidas, usando a nova função 'listar_bebidas'."""
    while True:
        print("\n--- Opções de Listagem ---")
        print("1 - Listar todas as bebidas")
        print("2 - Listar bebidas por código")
        print("3 - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            listar_bebidas() # Chamada sem argumentos para listar tudo
            break
        elif opcao == '2':
            if not estoque_bebidas:
                print("Nenhuma bebida cadastrada."); pausar(); break
            print("Digite os códigos das bebidas que deseja ver, separados por espaço.")
            indices_str = input("Códigos: ").strip().split()
            indices_para_listar = []
            for idx_str in indices_str:
                try:
                    indices_para_listar.append(int(idx_str) - 1)
                except ValueError:
                    print(f"'{idx_str}' não é um código válido e será ignorado.")
            if indices_para_listar:
                listar_bebidas(*indices_para_listar)
            else:
                print("Nenhum código válido foi fornecido."); pausar()
            break
        elif opcao == '3':
            break
        else:
            print("Opção inválida.")

def sua_sorte():
    global t
    if t == False:
        print("\n--- Teste sua sorte ---")
        print("\ncaso acerte o numero a seguir ganhará frete grátis")
        import random
        n = random.randint(1,5)
        print(f"\no valor tem que ser {type(n)}")
        x = int(input("\nEscolha um número entre 1 e 5: "))
        #print(type(x))
        if isinstance(x, int):
            if x <= 5 or x >= 1:
                if (x==n):
                    print("Parabens, você acertou e ganhou frete grátis!")
                else:
                    print(f"Que pena, você errou, o numero era {n}, tente novamente na próxima")
                t = True
    else:
        print("Você já testou sua sorte, tente novamente outra vez")

def menu_principal():
    print("\n--- Sistema da Loja de Bebidas ---")
    print("1 - Cadastrar bebida")
    print("2 - Lista de bebidas")
    print("3 - Comprar bebidas")
    print("4 - Teste sua sorte")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ").strip()
    if opcao == '1':
        cadastrar_bebida()
        menu_principal()
    elif opcao == '2':
        submenu_listar_bebidas()
        menu_principal()
    elif opcao == '3':
        vender_bebidas()
        menu_principal()
    elif opcao == '4':
        sua_sorte()
        menu_principal()
    elif opcao == '5':
        print("Saindo do sistema. Até logo!")
        return
    else:
        print("Opção inválida...")
        menu_principal()

# --- Ponto de Entrada do Programa ---
if __name__ == "__main__":
    menu_principal()