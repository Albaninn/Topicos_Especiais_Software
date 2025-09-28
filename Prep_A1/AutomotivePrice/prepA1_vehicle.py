import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path  #biblioteca para manipulação de caminhos

# ==============================================================================
# DEFINIÇÃO DE CAMINHOS
# ==============================================================================
# Caminho para o arquivo de dados
caminho_csv = Path("Prep_A1/AutomotivePrice/vehicle_price_prediction.csv")
# Pasta onde o CSV está localizado. As imagens serão salvas aqui.
pasta_destino = caminho_csv.parent

# ==============================================================================
# LEITURA E LIMPEZA DOS DADOS
# ==============================================================================

base = pd.read_csv(caminho_csv)
base.columns = base.columns.str.strip().str.replace('\n', '')
pd.set_option('display.max_columns', None)
colunas_para_remover = ['year', 'mileage_per_year', 'trim', 'brand_popularity']
base.drop(columns=colunas_para_remover, inplace=True)

print("Colunas removidas com sucesso! Colunas restantes no dataset:")
print(base.columns)
print("\n--- 1. Verificação de Valores Nulos (NaN) ---")
print(base.isnull().sum())
print("\n--- 2. Verificação de Valores Vazios ('') em colunas de texto ---")
for coluna in base.select_dtypes(include=['object']).columns:
    vazios = (base[coluna] == '').sum()
    if vazios > 0:
        print(f"Coluna '{coluna}' possui {vazios} valores vazios ('').")
print("\n--- 3. Verificação de Valores Zerados (0) em colunas numéricas ---")
valores_zerados = (base.select_dtypes(include=['number']) == 0).sum()
print(valores_zerados[valores_zerados > 0])
base['accident_history'].fillna('No Accidents', inplace=True)
print("\n--- Verificação de 'accident_history' após o tratamento ---")
print(base['accident_history'].value_counts())
print("\n--- Re-verificação de Valores Nulos ---")
print(base.isnull().sum())
print(base.describe())

# ==============================================================================
# GERAÇÃO DOS GRÁFICOS
# ==============================================================================

print("\n--- Gerando Gráficos de Composição ---")

# GRÁFICO 1: BARRAS HORIZONTAIS DAS MARCAS
contagem_marcas = base['make'].value_counts()
plt.figure(figsize=(12, 16))
sns.barplot(x=contagem_marcas.values, y=contagem_marcas.index, palette='viridis', orient='h')
for index, value in enumerate(contagem_marcas):
    plt.text(value, index, f' {value:,}'.replace(',', '.'), va='center', fontsize=10)
plt.title('Contagem de Veículos por Marca no Dataset', fontsize=18)
plt.xlabel('Quantidade de Veículos Listados', fontsize=12)
plt.ylabel('Marca', fontsize=12)
plt.tight_layout()
plt.savefig(pasta_destino / '1_barras_horizontais_marcas.png')
print("--> Gráfico 1 (barras_horizontais_marcas.png) salvo com sucesso!")

# GRÁFICO 2: PIZZA POR TIPO DE CARROCERIA
plt.figure(figsize=(10, 8))
contagem_carroceria = base['body_type'].value_counts()
plt.pie(contagem_carroceria, labels=contagem_carroceria.index, autopct='%1.1f%%', startangle=90, wedgeprops={"edgecolor":"black", 'linewidth': 0.5})
plt.title('Proporção por Tipo de Carroceria', fontsize=16)
plt.ylabel('')
plt.savefig(pasta_destino / '2_pizza_carroceria.png')
print("--> Gráfico 2 (pizza_carroceria.png) salvo com sucesso!")

# GRÁFICO 3: PIZZA POR TIPO DE TRANSMISSÃO
plt.figure(figsize=(8, 8))
contagem_transmissao = base['transmission'].value_counts()
plt.pie(contagem_transmissao, labels=contagem_transmissao.index, autopct='%1.1f%%', startangle=90, wedgeprops={"edgecolor":"black", 'linewidth': 0.5})
plt.title('Proporção por Tipo de Transmissão', fontsize=16)
plt.ylabel('')
plt.savefig(pasta_destino / '3_pizza_transmissao.png')
print("--> Gráfico 3 (pizza_transmissao.png) salvo com sucesso!")

# GRÁFICO 4: PIZZA POR TIPO DE COMBUSTÍVEL
plt.figure(figsize=(10, 8))
contagem_combustivel = base['fuel_type'].value_counts()
plt.pie(contagem_combustivel, labels=contagem_combustivel.index, autopct='%1.1f%%', startangle=90, wedgeprops={"edgecolor":"black", 'linewidth': 0.5})
plt.title('Proporção por Tipo de Combustível', fontsize=16)
plt.ylabel('')
plt.savefig(pasta_destino / '4_pizza_combustivel.png')
print("--> Gráfico 4 (pizza_combustivel.png) salvo com sucesso!")

print("\n--- Gerando Gráficos para Análise Exploratória ---")

# GRÁFICO 5: HISTOGRAMA DE PREÇOS
plt.figure(figsize=(12, 7))
sns.histplot(base['price'], bins=50, kde=True)
plt.title('Gráfico 5: Distribuição dos Preços dos Veículos', fontsize=16)
plt.xlabel('Preço (USD)', fontsize=12)
plt.ylabel('Quantidade', fontsize=12)
plt.ticklabel_format(style='plain', axis='x')
plt.savefig(pasta_destino / '5_histograma_precos.png')
print("--> Gráfico 5 (histograma_precos.png) salvo com sucesso!")

# GRÁFICO 6: DISPERSÃO DE PREÇO VS. QUILOMETRAGEM
amostra = base.sample(n=5000, random_state=42)
plt.figure(figsize=(12, 7))
sns.regplot(data=amostra, x='mileage', y='price', scatter_kws={'alpha':0.2}, line_kws={'color':'red', 'linewidth': 3})
plt.title('Gráfico 6: Relação entre Preço e Quilometragem', fontsize=16)
plt.xlabel('Quilometragem (Mileage)', fontsize=12)
plt.ylabel('Preço (USD)', fontsize=12)
plt.ticklabel_format(style='plain', axis='both')
plt.savefig(pasta_destino / '6_dispersao_preco_km.png')
print("--> Gráfico 6 (dispersao_preco_km.png) salvo com sucesso!")

# GRÁFICO 7: MAPA DE CALOR DAS CORRELAÇÕES
colunas_numericas = ['price', 'mileage', 'engine_hp', 'vehicle_age', 'owner_count']
df_numerico = base[colunas_numericas]
matriz_correlacao = df_numerico.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(matriz_correlacao, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Gráfico 7: Mapa de Calor das Correlações Numéricas', fontsize=16)
plt.savefig(pasta_destino / '7_heatmap_correlacoes.png')
print("--> Gráfico 7 (heatmap_correlacoes.png) salvo com sucesso!")

# GRÁFICO 8: CURVA DE DEPRECIAÇÃO GERAL
plt.figure(figsize=(14, 8))
sns.lineplot(data=base, x='vehicle_age', y='price', color='navy', linewidth=3)
plt.title('Gráfico 8: Curva de Depreciação Média Geral do Mercado', fontsize=16)
plt.xlabel('Idade do Veículo (Anos)', fontsize=12)
plt.ylabel('Preço Médio (USD)', fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.savefig(pasta_destino / '8_curva_depreciacao_geral.png')
print("--> Gráfico 8 (curva_depreciacao_geral.png) salvo com sucesso!")

# GRÁFICO 9: CURVA DE DEPRECIAÇÃO POR MARCA
top_4_marcas = base['make'].value_counts().nlargest(4).index
df_top_marcas = base[base['make'].isin(top_4_marcas)]
plt.figure(figsize=(14, 8))
sns.lineplot(data=df_top_marcas, x='vehicle_age', y='price', hue='make', errorbar=None, linewidth=3)
plt.title('Gráfico 9: Curva de Depreciação por Marca', fontsize=16)
plt.xlabel('Idade do Veículo (Anos)', fontsize=12)
plt.ylabel('Preço Médio (USD)', fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend(title='Marca', fontsize=11)
plt.savefig(pasta_destino / '9_curva_depreciacao_marcas.png')
print("--> Gráfico 9 (curva_depreciacao_marcas.png) salvo com sucesso!")

# plt.show() # Descomente para mostrar os gráficos na tela