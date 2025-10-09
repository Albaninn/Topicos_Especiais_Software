import sqlite3
import pandas as pd
from pathlib import Path

# ==============================================================================
# DEFINIÇÃO DE CAMINHOS
# ==============================================================================
# Cria o caminho para o arquivo do banco de dados na mesma pasta do CSV
caminho_csv = Path("Projeto_Fut/eur2024-2025/players_data-2024_2025.csv")
pasta_destino = caminho_csv.parent
caminho_db = pasta_destino / "euro_big5.db" # Nome do arquivo do banco de dados

# ==============================================================================
# LEITURA E LIMPEZA INICIAL DOS DADOS
# ==============================================================================

base = pd.read_csv(caminho_csv)
base.columns = base.columns.str.strip().str.replace('\n', '')
pd.set_option('display.max_columns', None)

print("--- Análise Inicial dos Dados ---")
print("Valores Nulos (NaN) antes do tratamento:")
print(base.isnull().sum())
