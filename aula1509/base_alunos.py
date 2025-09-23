import pandas as pd
from datetime import datetime

base = pd.read_csv("aula1509/forms2semestreup.csv") 

# --- PASSO 1: Limpar os nomes de TODAS as colunas de uma vez ---
# Isso remove espaços em branco no início/fim e substitui quebras de linha
base.columns = base.columns.str.strip().str.replace('\n', '')

# --- PASSO 2: Selecionar as colunas úteis ---
# Usamos .copy() para evitar avisos do pandas
df_analise = base[['DATA DE NASCIMENTO', 'Você possui trabalho ou estágio atualmente?']].copy()


# --- PASSO 3: Calcular a Idade ---
# Converte a coluna de data de nascimento para o formato de data, ignorando erros
# errors='coerce' transforma datas inválidas em NaT (Not a Time)
df_analise['DATA DE NASCIMENTO'] = pd.to_datetime(df_analise['DATA DE NASCIMENTO'], errors='coerce')

# Remove linhas onde a data de nascimento não pôde ser convertida
df_analise.dropna(subset=['DATA DE NASCIMENTO'], inplace=True)

# Calcula a idade em anos
hoje = datetime.now()
df_analise['IDADE'] = (hoje - df_analise['DATA DE NASCIMENTO']).dt.days / 365.25
df_analise['IDADE'] = df_analise['IDADE'].astype(int) # Converte para número inteiro

# --- PASSO 4: Fazer a "Correlação" (Análise) ---
# Vamos renomear a coluna para facilitar
df_analise.rename(columns={'Você possui trabalho ou estágio atualmente?': 'TRABALHA_OU_ESTAGIA'}, inplace=True)

# Primeiro, vamos ver quantos responderam "Sim" e "Não"
print("Total de alunos que trabalham/estagiam:")
print(df_analise['TRABALHA_OU_ESTAGIA'].value_counts())
print("-" * 50)

# Agora, a análise principal: agrupar por status de trabalho e ver as estatísticas da idade
print("Análise de Idade vs. Trabalho/Estágio:")
analise_idade_trabalho = df_analise.groupby('TRABALHA_OU_ESTAGIA')['IDADE'].describe()

print(analise_idade_trabalho)