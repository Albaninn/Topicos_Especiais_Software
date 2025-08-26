Instruções de Uso

Ao executar o programa, um menu principal será exibido com as seguintes opções:

1. Cadastrar Bebida
Escolha esta opção para adicionar um novo produto ao estoque.

O sistema solicitará, um por um, os seguintes dados: Nome da bebida, Marca, Tipo, Preço (R$), Volume (ml) e Quantidade em estoque.

2. Listar Bebidas
Esta opção exibe todos os produtos atualmente cadastrados no sistema.

A lista é numerada (começando em 1) e mostra todos os detalhes de cada bebida.

3. Vender Bebidas
Ao entrar nesta opção, o sistema primeiro mostra uma lista simplificada das bebidas disponíveis para venda.

Digite o número correspondente à bebida que deseja adicionar ao carrinho e, em seguida, a quantidade.

Após adicionar um item, o programa perguntará se você deseja adicionar outro (S para sim, N para não).

Ao finalizar a seleção, um resumo da venda será exibido, incluindo o subtotal, o desconto (se aplicável) e o valor total a pagar. O estoque será atualizado automaticamente.

4. Sair
Encerra a execução do programa.


==============================================================================================

Exemplo de Uso

PS C:\Users\cesar\Desktop\facul\UP\2025.2\Topicos_Especiais_Software> & "C:/Program Files/Inkscape/bin/python.exe" c:/Users/cesar/Desktop/facul/UP/2025.2/Topicos_Especiais_Software/Projeto_Bebidas/Loja.py

--- Sistema da Loja de Bebidas ---
1 - Cadastrar Bebida
2 - Listar Bebidas
3 - Vender Bebidas
4 - Sair
Escolha uma opção: 1

--- Cadastro de Bebida ---
Nome da bebida: Mango Loco
Marca: Monster
Tipo (ex: Cerveja, Vinho, Refrigerante): Energetico
Preço (R$): 12,00
Volume (ml): 473
Quantidade em estoque: 5

Bebida 'Mango Loco' cadastrada com sucesso!

Pressione ENTER para continuar...

--- Sistema da Loja de Bebidas ---
1 - Cadastrar Bebida
2 - Listar Bebidas
3 - Vender Bebidas
4 - Sair
Escolha uma opção: 1

--- Cadastro de Bebida ---
Nome da bebida: Coca Familia
Marca: CocaCola
Tipo (ex: Cerveja, Vinho, Refrigerante): Rerigerante
Preço (R$): 13
Volume (ml): 3000
Quantidade em estoque: 7

Bebida 'Coca Familia' cadastrada com sucesso!

Pressione ENTER para continuar...

--- Sistema da Loja de Bebidas ---
1 - Cadastrar Bebida
2 - Listar Bebidas
3 - Vender Bebidas
4 - Sair
Escolha uma opção: 2

--- Estoque de Bebidas ---
[1] - Nome: Mango Loco (Monster)
      Tipo: Energetico
      Volume: 473ml
      Preço: R$ 12.00
      Estoque: 5 unidades
-------------------------
[2] - Nome: Coca Familia (CocaCola)
      Tipo: Rerigerante
      Volume: 3000ml
      Preço: R$ 13.00
      Estoque: 7 unidades
-------------------------

Pressione ENTER para continuar... 

--- Sistema da Loja de Bebidas ---
1 - Cadastrar Bebida
2 - Listar Bebidas
3 - Vender Bebidas
4 - Sair
Escolha uma opção: 3

--- Venda de Bebidas ---
Bebidas disponíveis:
[1] Mango Loco - Estoque: 5 - R$ 12.00
[2] Coca Familia - Estoque: 7 - R$ 13.00

Digite o número da bebida que deseja comprar (ou pressione ENTER para finalizar): 1
Digite a quantidade de 'Mango Loco' (disponível: 5): 4
4x 'Mango Loco' adicionado(s) ao carrinho.
Deseja adicionar outra bebida? [S/N]: s

Digite o número da bebida que deseja comprar (ou pressione ENTER para finalizar): 3
Número de bebida inválido. Tente novamente.

Digite o número da bebida que deseja comprar (ou pressione ENTER para finalizar): 2
Digite a quantidade de 'Coca Familia' (disponível: 7): 7
7x 'Coca Familia' adicionado(s) ao carrinho.
Deseja adicionar outra bebida? [S/N]: s

Digite o número da bebida que deseja comprar (ou pressione ENTER para finalizar):

--- Resumo da Venda ---
4x 'Mango Loco' (R$ 12.00) = R$ 48.00
7x 'Coca Familia' (R$ 13.00) = R$ 91.00

------------------------------
Subtotal: R$ 139.00
Desconto (10.5%): R$ 14.59
TOTAL A PAGAR: R$ 124.41
------------------------------

Venda finalizada com sucesso!

Pressione ENTER para continuar...

--- Sistema da Loja de Bebidas ---
1 - Cadastrar Bebida
2 - Listar Bebidas
3 - Vender Bebidas
4 - Sair
Escolha uma opção: 2

--- Estoque de Bebidas ---
[1] - Nome: Mango Loco (Monster)
      Tipo: Energetico
      Volume: 473ml
      Preço: R$ 12.00
      Estoque: 1 unidades
-------------------------
[2] - Nome: Coca Familia (CocaCola)
      Tipo: Rerigerante
      Volume: 3000ml
      Preço: R$ 13.00
      Estoque: 0 unidades
-------------------------

Pressione ENTER para continuar...

--- Sistema da Loja de Bebidas ---
1 - Cadastrar Bebida
2 - Listar Bebidas
3 - Vender Bebidas
4 - Sair
Escolha uma opção: 4
Saindo do sistema. Até logo!