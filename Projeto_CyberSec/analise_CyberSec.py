import sqlite3
import pandas as pd
from pathlib import Path
import glob # Biblioteca para encontrar arquivos que correspondem a um padrão
import zipfile # Biblioteca para manipular arquivos ZIP

# ==============================================================================
# DEFINIÇÃO DE CAMINHOS
# ==============================================================================
# Caminho da pasta do projeto principal
caminho_projeto = Path("Projeto_CyberSec")
# Caminho do arquivo ZIP
caminho_zip = caminho_projeto / "IDS2018.zip"
# O caminho para a PASTA onde os arquivos CSV ficarão
caminho_pasta_csv = caminho_projeto / "IDS2018"
# Caminho para o arquivo do banco de dados (agora dentro da pasta dos CSVs)
caminho_db = caminho_pasta_csv / "DDoS2018.db" 
NOME_TABELA = 'DDoS_data' # Nome da nossa tabela no DB

# ==============================================================================
# ETAPA 0: DESCOMPACTAR OS DADOS (SE NECESSÁRIO)
# ==============================================================================
print(f"--- Verificando a necessidade de descompactação ---")
# Cria a pasta de destino se ela não existir
caminho_pasta_csv.mkdir(exist_ok=True)
# Verifica se já existem arquivos CSV na pasta de destino
arquivos_csv_existentes = glob.glob(str(caminho_pasta_csv / "*.csv"))

if not arquivos_csv_existentes and caminho_zip.exists():
    print(f"Arquivos CSV não encontrados. Descompactando '{caminho_zip.name}' para '{caminho_pasta_csv}'...")
    with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
        zip_ref.extractall(caminho_pasta_csv)
    print("Arquivos descompactados com sucesso!")
elif not arquivos_csv_existentes and not caminho_zip.exists():
    print(f"ERRO: A pasta '{caminho_pasta_csv}' está vazia e o arquivo '{caminho_zip.name}' não foi encontrado.")
    # Encerra o script se não houver dados para processar
    exit()
else:
    print("Arquivos CSV já existem na pasta. Pulando a descompactação.")

# ==============================================================================
# VERIFICAÇÃO E CRIAÇÃO DO BANCO DE DADOS (SE NECESSÁRIO)
# ==============================================================================

# Verifica se o arquivo de banco de dados já existe.
if caminho_db.exists():
    print(f"\nO banco de dados '{caminho_db.name}' já existe. Pulando a etapa de criação.")
else:
    print(f"\nO banco de dados '{caminho_db.name}' não foi encontrado. Iniciando o processo de criação...")

    # ==============================================================================
    # 1. PRÉ-ANÁLISE: DESCOBRIR TODAS AS COLUNAS DE TODOS OS ARQUIVOS
    # ==============================================================================
    print("\n--- Analisando cabeçalhos de todos os arquivos... ---")
    lista_arquivos_csv = glob.glob(str(caminho_pasta_csv / "*.csv"))
    colunas_master = set()

    for arquivo in lista_arquivos_csv:
        # Lê apenas o cabeçalho (primeira linha) para pegar os nomes das colunas
        df_header = pd.read_csv(arquivo, nrows=0, low_memory=False)
        # Limpa os nomes das colunas
        df_header.columns = df_header.columns.str.strip().str.replace('\n', '')
        # Adiciona as colunas deste arquivo ao nosso conjunto de colunas mestras
        colunas_master.update(df_header.columns)

    # Converte o conjunto para uma lista para manter a ordem
    master_columns_list = sorted(list(colunas_master))
    print(f"Análise concluída. Total de colunas únicas encontradas: {len(master_columns_list)}")

    # ==============================================================================
    # 2. CRIAÇÃO DA TABELA MESTRA E INSERÇÃO DOS DADOS
    # ==============================================================================
    conn = sqlite3.connect(caminho_db)

    # Cria a tabela com a estrutura completa, mas vazia
    # Usamos um DataFrame vazio com todas as colunas mestras para definir o schema
    df_vazio = pd.DataFrame(columns=master_columns_list)
    df_vazio.to_sql(NOME_TABELA, conn, if_exists='replace', index=False)
    print(f"\nTabela '{NOME_TABELA}' criada com sucesso no banco de dados.")

    # Agora, processamos os arquivos e inserimos os dados
    for arquivo in lista_arquivos_csv:
        print(f"\nProcessando o arquivo em pedaços: {Path(arquivo).name}...")
        
        chunk_reader = pd.read_csv(arquivo, chunksize=100000, low_memory=False)
        
        for i, chunk in enumerate(chunk_reader):
            print(f"  - Preparando e escrevendo pedaço {i+1}...")
            
            # Limpa os nomes das colunas do chunk atual
            chunk.columns = chunk.columns.str.strip().str.replace('\n', '')
            
            # *** A MÁGICA ACONTECE AQUI ***
            # Reindexa o chunk para que ele tenha EXATAMENTE as mesmas colunas da tabela mestra.
            # Colunas que existem no chunk mas não na master são descartadas (se houver).
            # Colunas que existem na master mas não no chunk são adicionadas com valor Nulo (NaN).
            chunk_reindexado = chunk.reindex(columns=master_columns_list)
            
            # Anexa o chunk ajustado à tabela no banco de dados
            chunk_reindexado.to_sql(NOME_TABELA, conn, if_exists='append', index=False)

    conn.close()

    print(f"\n\n--- Processo Concluído! ---")
    print(f"Todos os dados foram salvos com sucesso na tabela '{NOME_TABELA}'.")

# ==============================================================================
# EXIBIÇÃO DO ESQUEMA DA TABELA (SEMPRE EXECUTA)
# ==============================================================================
print("\n" + "="*70)
print(f"--- Lendo e exibindo o esquema da tabela '{NOME_TABELA}' ---")
try:
    conn = sqlite3.connect(caminho_db)
    query = f"PRAGMA table_info('{NOME_TABELA}');"
    schema_df = pd.read_sql_query(query, conn)
    conn.close()

    print("\n--- Colunas e Tipos de Dados ---")
    pd.set_option('display.max_rows', None)
    print(schema_df[['name', 'type']])

except Exception as e:
    print(f"\nOcorreu um erro ao ler o esquema: {e}")

# ==============================================================================
# ANÁLISE DE NULOS E SUGESTÃO DE TIPOS (NOVO BLOCO)
# ==============================================================================
print("\n" + "="*70)
print("--- Análise de Amostra: Verificação de Nulos e Sugestão de Tipos ---")
print("Analisando uma amostra dos dados para otimizar a performance...")

try:
    conn = sqlite3.connect(caminho_db)
    # Para não carregar tudo, pegamos uma amostra de 200.000 linhas
    SAMPLE_SIZE = 200000
    query_amostra = f"SELECT * FROM {NOME_TABELA} LIMIT {SAMPLE_SIZE}"
    df_amostra = pd.read_sql_query(query_amostra, conn)
    conn.close()

    print(f"\nAmostra de {len(df_amostra)} linhas carregada com sucesso.")

    # --- 1. Validação de Nulos e Vazios ---
    print("\n--- Verificando colunas com valores nulos ou vazios na amostra ---")
    colunas_com_nulos = []
    for col in df_amostra.columns:
        # Conta tanto nulos (NaN) quanto strings vazias ''
        nulos_count = df_amostra[col].isnull().sum()
        if nulos_count > 0:
            print(f"- Coluna '{col}': {nulos_count} valores nulos/vazios encontrados.")
            colunas_com_nulos.append(col)
    
    if not colunas_com_nulos:
        print("Nenhuma coluna com valores nulos ou vazios foi encontrada na amostra.")

    # --- 2. Análise e Sugestão de Tipos de Dados ---
    print("\n--- Analisando e sugerindo tipos de dados corretos ---")
    dtype_sugerido = {}
    for col in df_amostra.columns:
        tipo_original = df_amostra[col].dtype
        # Tenta converter a coluna para um tipo numérico.
        # errors='coerce' transforma o que não for número em NaN (Nulo)
        coluna_convertida = pd.to_numeric(df_amostra[col], errors='coerce')
        novo_tipo = coluna_convertida.dtype

        # Se o tipo mudou de 'object' (texto) para numérico, a conversão foi um sucesso!
        if tipo_original == 'object' and novo_tipo != 'object':
            print(f"- Coluna '{col}': pode ser convertida de TEXT para {novo_tipo}.")
            # Se não houver valores nulos após a conversão, pode ser inteiro
            if coluna_convertida.isnull().sum() == 0:
                dtype_sugerido[col] = 'integer'
            else:
                dtype_sugerido[col] = 'float'
        else:
            # Mantém o tipo original se não for conversível ou se já for numérico
            dtype_sugerido[col] = tipo_original

    print("\n--- Dicionário de Tipos Sugerido para seus próximos scripts ---")
    print("Você pode usar este dicionário para carregar os dados já com os tipos corretos:")
    # Formata o dicionário para ficar fácil de copiar e colar
    dtype_map_str = "dtype_map = {\n"
    for col, tipo in dtype_sugerido.items():
        dtype_map_str += f"    '{col}': '{str(tipo)}',\n"
    dtype_map_str += "}"
    print(dtype_map_str)

except Exception as e:
    print(f"\nOcorreu um erro durante a análise da amostra: {e}")