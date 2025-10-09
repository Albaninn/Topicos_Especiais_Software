import sqlite3
import pandas as pd
from pathlib import Path

# ==============================================================================
# DEFINIÇÃO DE CAMINHOS
# ==============================================================================
# Cria o caminho para o arquivo do banco de dados na mesma pasta do CSV
caminho_csv = Path("Projeto_CyberSec/CyberSec/Global_Cybersecurity_Threats_2015-2024.csv")
pasta_destino = caminho_csv.parent
caminho_db = pasta_destino / "CyberSec.db" # Nome do arquivo do banco de dados

# ==============================================================================
# LEITURA E LIMPEZA INICIAL DOS DADOS
# ==============================================================================

base = pd.read_csv(caminho_csv)
base.columns = base.columns.str.strip().str.replace('\n', '')
pd.set_option('display.max_columns', None)

print("--- Análise Inicial dos Dados ---")
print("Valores Nulos (NaN) antes do tratamento:")
print(base.isnull().sum())
