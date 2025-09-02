# Sistema de Gestão para Loja de Bebidas

Este é um projeto de faculdade desenvolvido em Python que simula um sistema de ponto de venda (PDV) e gestão de estoque para uma pequena loja de bebidas. O sistema opera inteiramente via terminal e foi **modularizado em dois arquivos** para separar responsabilidades e demonstrar conceitos mais avançados de Python, como o uso de funções como argumentos (cidadãos de primeira classe), desempacotamento de parâmetros e funções lambda.

## 📜 Descrição do Sistema

O programa oferece um menu interativo com as funcionalidades essenciais para o gerenciamento de uma loja. A lógica principal de interação com o usuário está no arquivo `MAIN.py`, enquanto a regra de negócio específica para o cálculo de descontos foi isolada no módulo `desconto_padrao_da_loja.py`.

## ✨ Funcionalidades

  - **Cadastro de Produtos:** Permite adicionar novas bebidas ao sistema com seus respectivos detalhes.
  - **Listagem de Estoque Avançada:** Permite visualizar todos os produtos de uma vez ou buscar itens específicos por seus códigos.
  - **Sistema de Venda:**
      - Interface para selecionar produtos e quantidades, com validação de estoque.
      - Cálculo de subtotal e aplicação de desconto condicional, cuja lógica é importada de um módulo externo.
      - Atualização automática do estoque após cada venda.
  - **Mini-game "Teste sua Sorte":** Uma funcionalidade extra onde o usuário pode tentar adivinhar um número para ganhar um prêmio simbólico (frete grátis).

## 📁 Estrutura do Projeto

O projeto está organizado nos seguintes arquivos:

  - `MAIN.py`: Arquivo principal que contém toda a lógica de interação com o usuário, menus, cadastro, listagem, venda e controle de estoque. Ele atua como o ponto de entrada da aplicação.
  - `desconto_padrao_da_loja.py`: Módulo que contém exclusivamente a lógica de cálculo de desconto, implementada como uma função lambda. Este módulo é importado pelo `MAIN.py`.

## 🚀 Como Rodar o Projeto

Para executar o sistema, você precisa ter o Python 3 instalado e os dois arquivos do projeto na mesma pasta.

**Passos para Execução:**

1.  **Garanta a Estrutura de Arquivos:**
    Certifique-se de que os dois arquivos, `MAIN.py` e `desconto_padrao_da_loja.py`, estão localizados no **mesmo diretório**.

2.  **Abra o Terminal:**
    Abra o seu terminal de linha de comando (Prompt de Comando, PowerShell, Terminal, etc.).

3.  **Navegue até a Pasta do Projeto:**
    Use o comando `cd` para navegar até o diretório onde você salvou os arquivos.

    ```bash
    # Exemplo:
    cd C:\Caminho\Para\Sua\Pasta
    ```

4.  **Execute o Script Principal:**
    Para iniciar o programa, execute o arquivo `MAIN.py`:

    ```bash
    python MAIN.py
    ```

    O sistema será iniciado e o menu principal será exibido no terminal.

## 📖 Instruções de Uso

Ao executar o programa, o menu principal oferecerá 5 opções:

### 1\. Cadastrar Bebida

  - Adiciona um novo produto ao estoque, solicitando dados como nome, marca, preço, etc.

### 2\. Listar Bebidas

  - Esta opção abre um **submenu de listagem**:
      - **Opção 1:** Lista todas as bebidas cadastradas.
      - **Opção 2:** Permite que você digite os códigos dos produtos (separados por espaço) para ver apenas os itens selecionados.

### 3\. Vender Bebidas

  - Inicia o processo de venda, onde você pode adicionar itens ao carrinho, definir quantidades e finalizar a compra. O desconto será calculado e aplicado automaticamente conforme a regra do módulo `desconto_padrao_da_loja.py`.

### 4\. Teste sua Sorte

  - Inicia um mini-game onde você tenta adivinhar um número de 1 a 10.

### 5\. Sair

  - Encerra a execução do programa.


##############################################################################################

C:\Users\cesar\Desktop\facul\UP\2025.2\Topicos_Especiais_Software> & "C:/Program Files/Inkscape/bin/python.exe" c:/Users/cesar/Desktop/facul/UP/2025.2/Topicos_Especiais_Software/Projeto_Bebidas/drink-project/main.py

--- Sistema da Loja de Bebidas ---
1 - Cadastrar bebida
2 - Lista de bebidas
3 - Comprar bebidas
4 - Teste sua sorte
5 - Sair
Escolha uma opção: 1

--- Cadastro de Bebida ---
Nome da bebida: Putona
Marca: Coca Cola
Tipo (ex: Cerveja, Vinho, Refrigerante): Refrigerante
Preço (R$): 13
Volume (ml): 3000
Quantidade em estoque: 123

Bebida 'Putona' cadastrada com sucesso!

Pressione ENTER para continuar...

--- Sistema da Loja de Bebidas ---
1 - Cadastrar bebida
2 - Lista de bebidas
3 - Comprar bebidas
4 - Teste sua sorte
5 - Sair
Escolha uma opção: 1

--- Cadastro de Bebida ---
Nome da bebida: Mango Loco
Marca: Monster
Tipo (ex: Cerveja, Vinho, Refrigerante): Energetico
Preço (R$): 9
Volume (ml): 473
Quantidade em estoque: 43

Bebida 'Mango Loco' cadastrada com sucesso!

Pressione ENTER para continuar...

--- Sistema da Loja de Bebidas ---
1 - Cadastrar bebida
2 - Lista de bebidas
3 - Comprar bebidas
4 - Teste sua sorte
5 - Sair
Escolha uma opção: 2

--- Opções de Listagem ---
1 - Listar todas as bebidas
2 - Listar bebidas por código
3 - Voltar ao menu principal
Escolha uma opção: 1

--- Estoque de Bebidas ---
[1] - Nome: Putona (Coca Cola)
      Preço: R$ 13.00 | Estoque: 123 unidades
-------------------------
[2] - Nome: Mango Loco (Monster)
      Preço: R$ 9.00 | Estoque: 43 unidades
-------------------------

Pressione ENTER para continuar...

--- Sistema da Loja de Bebidas ---
1 - Cadastrar bebida
2 - Lista de bebidas
3 - Comprar bebidas
4 - Teste sua sorte
5 - Sair
Escolha uma opção: 2

--- Opções de Listagem ---
1 - Listar todas as bebidas
2 - Listar bebidas por código
3 - Voltar ao menu principal
Escolha uma opção: 2
Digite os códigos das bebidas que deseja ver, separados por espaço.
Códigos: 2

--- Estoque de Bebidas ---
[2] - Nome: Mango Loco (Monster)
      Preço: R$ 9.00 | Estoque: 43 unidades
-------------------------

Pressione ENTER para continuar...

--- Sistema da Loja de Bebidas ---
1 - Cadastrar bebida
2 - Lista de bebidas
3 - Comprar bebidas
4 - Teste sua sorte
5 - Sair
Escolha uma opção: 3

--- Venda de Bebidas ---
Bebidas disponíveis:
[1] Putona - Estoque: 123 - R$ 13.00
[2] Mango Loco - Estoque: 43 - R$ 9.00

Digite o número da bebida (ou ENTER para finalizar): 1
Quantidade de 'Putona' (disp: 123): 32
32x 'Putona' adicionado(s).
Adicionar outra bebida? [S/N]: s

Digite o número da bebida (ou ENTER para finalizar): 2
Quantidade de 'Mango Loco' (disp: 43): 31
31x 'Mango Loco' adicionado(s).
Adicionar outra bebida? [S/N]: n

--- Resumo da Venda ---
32x 'Putona' (R$ 13.00) = R$ 416.00
31x 'Mango Loco' (R$ 9.00) = R$ 279.00

------------------------------
Subtotal: R$ 695.00
Desconto (10.5%): R$ 72.97
TOTAL A PAGAR: R$ 622.02
------------------------------

Venda finalizada com sucesso!

Pressione ENTER para continuar...

--- Sistema da Loja de Bebidas ---
1 - Cadastrar bebida
2 - Lista de bebidas
3 - Comprar bebidas
4 - Teste sua sorte
5 - Sair
Escolha uma opção: 2

--- Opções de Listagem ---
1 - Listar todas as bebidas
2 - Listar bebidas por código
3 - Voltar ao menu principal
Escolha uma opção: 1

--- Estoque de Bebidas ---
[1] - Nome: Putona (Coca Cola)
      Preço: R$ 13.00 | Estoque: 91 unidades
-------------------------
[2] - Nome: Mango Loco (Monster)
      Preço: R$ 9.00 | Estoque: 12 unidades
-------------------------

Pressione ENTER para continuar...

--- Sistema da Loja de Bebidas ---
1 - Cadastrar bebida
2 - Lista de bebidas
3 - Comprar bebidas
4 - Teste sua sorte
5 - Sair
Escolha uma opção: 4

--- Teste sua sorte ---

caso acerte o numero a seguir ganhará frete grátis

o valor tem que ser <class 'int'>

Escolha um número entre 1 e 5: 2
Que pena, você errou, o numero era 1, tente novamente na próxima

--- Sistema da Loja de Bebidas ---
1 - Cadastrar bebida
2 - Lista de bebidas
3 - Comprar bebidas
4 - Teste sua sorte
5 - Sair
Escolha uma opção: 4
Você já testou sua sorte, tente novamente outra vez

--- Sistema da Loja de Bebidas ---
1 - Cadastrar bebida
2 - Lista de bebidas
3 - Comprar bebidas
4 - Teste sua sorte
5 - Sair
Escolha uma opção: 5
Saindo do sistema. Até logo!