import sqlite3
import pandas as pd
from pathlib import Path

# ==============================================================================
# DEFINIÇÃO DE CAMINHOS
# ==============================================================================
# Cria o caminho para o arquivo do banco de dados na mesma pasta do CSV
caminho_csv = Path("Projeto_Fut/Brasileirão2024/database.csv")
pasta_destino = caminho_csv.parent
caminho_db = pasta_destino / "brasileirao.db" # Nome do arquivo do banco de dados

# ==============================================================================
# LEITURA E LIMPEZA INICIAL DOS DADOS
# ==============================================================================

base = pd.read_csv(caminho_csv)
base.columns = base.columns.str.strip().str.replace('\n', '')
pd.set_option('display.max_columns', None)

print("--- Análise Inicial dos Dados ---")
print("Valores Nulos (NaN) antes do tratamento:")
print(base.isnull().sum())


# ==============================================================================
# TRATAMENTO DE DADOS NULOS (SUGESTÃO)
# ==============================================================================
# Para colunas numéricas, uma estratégia comum é preencher com a mediana ou 0
# Usaremos 0 aqui, pois faz sentido para estatísticas de jogo não registradas.
colunas_numericas_nulas = ['Min.', 'Contatos', 'Div', 'Bloqueios', 'xG', 'npxG', 'xAG', 'SCA', 'GCA', 'Cmp', 'Att', 'Cmp%', 'PrgP', 'Conduções', 'PrgC', 'Tent', 'Suc']
for coluna in colunas_numericas_nulas:
    # A verificação 'if coluna in base.columns' garante que o código não quebre se a coluna não existir
    if coluna in base.columns:
        base[coluna].fillna(0, inplace=True)

# Para colunas de texto (categóricas), podemos usar uma string como "Não Informado"
if 'Nação' in base.columns:
    base['Nação'].fillna('Não Informado', inplace=True)
    
# Tratamento para colunas 'Idade' e 'Nação' que possuem 6 valores nulos
# Pode ser mais interessante remover as linhas, já que são poucas e podem ser de registros inválidos
base.dropna(subset=['Idade', 'Nação'], inplace=True)


print("\nValores Nulos (NaN) após o tratamento:")
print(base.isnull().sum())


# ==============================================================================
# CONEXÃO E ARMAZENAMENTO NO SQLITE
# ==============================================================================
try:
    # 1. Cria a conexão com o banco de dados.
    # O arquivo .db será criado se não existir.
    conexao = sqlite3.connect(caminho_db)

    # 2. Salva o DataFrame em uma tabela no banco de dados.
    # - 'jogadores_2024' é o nome que daremos para a tabela.
    # - if_exists='replace' significa que se a tabela já existir, ela será substituída.
    #   (Útil durante o desenvolvimento. Use 'append' se quiser adicionar novos dados sem apagar os antigos).
    base.to_sql('jogadores_2024', conexao, if_exists='replace', index=False)

    print(f"\n[SUCESSO] Dados salvos com sucesso no banco de dados '{caminho_db.name}'")
    print(f"Tabela 'jogadores_2024' criada/substituída.")

except Exception as e:
    print(f"[ERRO] Ocorreu um erro ao salvar os dados: {e}")

finally:
    # 3. Fecha a conexão com o banco de dados.
    if 'conexao' in locals() and conexao:
        conexao.close()


# ==============================================================================
# EXEMPLO: LENDO DADOS DE VOLTA DO SQLITE PARA O PANDAS
# ==============================================================================
try:
    conexao = sqlite3.connect(caminho_db)
    cursor = conexao.cursor()

    # Query para selecionar os 5 jogadores com mais gols
    query = "SELECT Jogador, Time, Gols FROM jogadores_2024 ORDER BY Gols DESC LIMIT 5"
    
    # pd.read_sql_query executa a query e já retorna um DataFrame
    top_5_artilheiros = pd.read_sql_query(query, conexao)

    print("\n--- Exemplo de Consulta no Banco de Dados ---")
    print("Top 5 Artilheiros do Brasileirão 2024:")
    print(top_5_artilheiros)

except Exception as e:
    print(f"[ERRO] Ocorreu um erro ao consultar os dados: {e}")

finally:
    if 'conexao' in locals() and conexao:
        conexao.close()
