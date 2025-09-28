import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base = pd.read_csv("Prep_A1/AutomotivePrice/vehicle_price_prediction.csv")

base.columns = base.columns.str.strip().str.replace('\n', '')

pd.set_option('display.max_columns', None)

# Lista das colunas para remover
colunas_para_remover = ['year', 'mileage_per_year', 'trim', 'brand_popularity']

base.drop(columns=colunas_para_remover, inplace=True)

print("Colunas removidas com sucesso! Colunas restantes no dataset:")
print(base.columns)

print("\n--- 1. Verificação de Valores Nulos (NaN) ---")
# O comando .isnull().sum() conta a quantidade de valores nulos em cada coluna
print(base.isnull().sum())


print("\n--- 2. Verificação de Valores Vazios ('') em colunas de texto ---")
# Itera apenas sobre as colunas do tipo 'object' (texto)
for coluna in base.select_dtypes(include=['object']).columns:
    # Conta quantos valores são exatamente uma string vazia
    vazios = (base[coluna] == '').sum()
    if vazios > 0:
        print(f"Coluna '{coluna}' possui {vazios} valores vazios ('').")


print("\n--- 3. Verificação de Valores Zerados (0) em colunas numéricas ---")
# Seleciona apenas colunas numéricas, verifica quais valores são iguais a 0 e soma
valores_zerados = (base.select_dtypes(include=['number']) == 0).sum()

# Filtra o resultado para mostrar apenas as colunas que realmente possuem valores zerados
print(valores_zerados[valores_zerados > 0])

# Preenche os valores nulos na coluna 'accident_history' com a string 'No Accidents'
base['accident_history'].fillna('No Accidents', inplace=True)

print("\n--- Verificação de 'accident_history' após o tratamento ---")
# O .value_counts() vai te mostrar quantas ocorrências existem de cada categoria
print(base['accident_history'].value_counts())

# Confirmação final de que não há mais nulos
print("\n--- Re-verificação de Valores Nulos ---")
print(base.isnull().sum())

# Gera estatísticas descritivas para todas as colunas numéricas
print(base.describe())

print("\n--- Gerando Gráficos de Pizza para Análise de Composição ---")

# ==============================================================================
# GRÁFICO 1: GRÁFICO DE BARRAS HORIZONTAIS DAS MARCAS (make)
# ==============================================================================
# Propósito: Mostrar a frequência de TODAS as marcas de forma clara e ordenada.

# 1. Conta a ocorrência de cada marca. O value_counts() já ordena do maior para o menor.
contagem_marcas = base['make'].value_counts()
# 2. Define o tamanho da figura. A altura (segundo número) é maior para caber todas as marcas.
plt.figure(figsize=(12, 16))
# 3. Cria o gráfico de barras horizontais.
#    - No eixo Y, colocamos os nomes das marcas (contagem_marcas.index).
#    - No eixo X, colocamos os valores da contagem (contagem_marcas.values).
sns.barplot(x=contagem_marcas.values, y=contagem_marcas.index, palette='viridis', orient='h')
# 4. Adiciona o valor exato no final de cada barra para clareza
#    Este loop passa por cada barra e escreve o valor ao lado dela.
for index, value in enumerate(contagem_marcas):
    plt.text(value, index, f' {value:,}'.replace(',', '.'), va='center', fontsize=10)
# 5. Adiciona títulos e rótulos para o gráfico ficar completo
plt.title('Contagem de Veículos por Marca no Dataset', fontsize=18)
plt.xlabel('Quantidade de Veículos Listados', fontsize=12)
plt.ylabel('Marca', fontsize=12)
# Ajusta o layout para garantir que nada seja cortado
plt.tight_layout()
# 6. Salva o novo gráfico
plt.savefig('1_barras_horizontais_marcas.png')
print("--> Gráfico de barras de Marcas (1_barras_horizontais_marcas.png) salvo com sucesso!")



# ==============================================================================
# GRÁFICO 2: DISTRIBUIÇÃO POR TIPO DE CARROCERIA (body_type)
# ==============================================================================
plt.figure(figsize=(10, 8))
contagem_carroceria = base['body_type'].value_counts()
plt.pie(contagem_carroceria, labels=contagem_carroceria.index, autopct='%1.1f%%', startangle=90,
        wedgeprops={"edgecolor":"black", 'linewidth': 0.5})
plt.title('Proporção por Tipo de Carroceria', fontsize=16)
plt.ylabel('')
plt.savefig('2_pizza_carroceria.png')
print("--> Gráfico de pizza de Carroceria (2_pizza_carroceria.png) salvo com sucesso!")


# ==============================================================================
# GRÁFICO 3: DISTRIBUIÇÃO POR TIPO DE TRANSMISSÃO (transmission)
# ==============================================================================
plt.figure(figsize=(8, 8))
contagem_transmissao = base['transmission'].value_counts()
plt.pie(contagem_transmissao, labels=contagem_transmissao.index, autopct='%1.1f%%', startangle=90,
        wedgeprops={"edgecolor":"black", 'linewidth': 0.5})
plt.title('Proporção por Tipo de Transmissão', fontsize=16)
plt.ylabel('')
plt.savefig('3_pizza_transmissao.png')
print("--> Gráfico de pizza de Transmissão (3_pizza_transmissao.png) salvo com sucesso!")


# ==============================================================================
# GRÁFICO 4: DISTRIBUIÇÃO POR TIPO DE COMBUSTÍVEL (fuel_type)
# ==============================================================================
plt.figure(figsize=(10, 8))
contagem_combustivel = base['fuel_type'].value_counts()
plt.pie(contagem_combustivel, labels=contagem_combustivel.index, autopct='%1.1f%%', startangle=90,
        wedgeprops={"edgecolor":"black", 'linewidth': 0.5})
plt.title('Proporção por Tipo de Combustível', fontsize=16)
plt.ylabel('')
plt.savefig('4_pizza_combustivel.png')
print("--> Gráfico de pizza de Combustível (4_pizza_combustivel.png) salvo com sucesso!")


print("\n--- Gerando Gráficos para Análise Exploratória ---")

# ==============================================================================
# GRÁFICO 5: Histograma da Distribuição de Preços
# ==============================================================================
# Propósito: Entender a faixa de preço mais comum e a distribuição geral dos valores.

plt.figure(figsize=(12, 7))  # Cria uma figura com tamanho customizado
sns.histplot(base['price'], bins=50, kde=True)  # Cria o histograma com 50 barras e uma linha de densidade
plt.title('Gráfico 5: Distribuição dos Preços dos Veículos', fontsize=16)
plt.xlabel('Preço (USD)', fontsize=12)
plt.ylabel('Quantidade', fontsize=12)
plt.ticklabel_format(style='plain', axis='x') # Evita notação científica no eixo X
plt.savefig('5_histograma_precos.png')  # Salva o gráfico em um arquivo de imagem
print("--> Gráfico 5 (histograma_precos.png) salvo com sucesso!")


# ==============================================================================
# GRÁFICO 6: Gráfico de Dispersão de Preço vs. Quilometragem
# ==============================================================================
# Propósito: Visualizar a correlação negativa entre o preço e a quilometragem.

# NOTA: Como o dataset é muito grande, plotar todos os pontos pode deixar o gráfico
# lento e poluído. Vamos usar uma amostra aleatória de 5000 pontos para ver a tendência.
amostra = base.sample(n=5000, random_state=42)

plt.figure(figsize=(12, 7))
sns.regplot(data=amostra, x='mileage', y='price',
            scatter_kws={'alpha':0.2}, # Deixa os pontos mais transparentes
            line_kws={'color':'red', 'linewidth': 3}) # Deixa a linha de tendência vermelha e mais grossa
plt.title('Gráfico 6: Relação entre Preço e Quilometragem', fontsize=16)
plt.xlabel('Quilometragem (Mileage)', fontsize=12)
plt.ylabel('Preço (USD)', fontsize=12)
plt.ticklabel_format(style='plain', axis='both')
plt.savefig('6_dispersao_preco_km.png')
print("--> Gráfico 6 (dispersao_preco_km.png) salvo com sucesso!")


# ==============================================================================
# GRÁFICO 7: MAPA DE CALOR DAS CORRELAÇÕES
# ==============================================================================
# Propósito: Mostrar um resumo técnico da força das relações entre as
#            principais variáveis numéricas do dataset.

# 1. Seleciona apenas as colunas numéricas de interesse
colunas_numericas = ['price', 'mileage', 'engine_hp', 'vehicle_age', 'owner_count']
df_numerico = base[colunas_numericas]
# 2. Calcula a matriz de correlação
matriz_correlacao = df_numerico.corr()
# 3. Cria o gráfico do tipo heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(matriz_correlacao,
            annot=True,          # Mostra os números dentro de cada célula
            cmap='coolwarm',     # Usa um mapa de cores "frio" para negativo e "quente" para positivo
            fmt=".2f",           # Formata os números para terem 2 casas decimais
            linewidths=.5)
plt.title('Gráfico 7: Mapa de Calor das Correlações Numéricas', fontsize=16)
plt.savefig('7_heatmap_correlacoes.png')
print("--> Gráfico 7 (heatmap_correlacoes.png) salvo com sucesso!")


# ==============================================================================
# GRÁFICO 8: CURVA DE DEPRECIAÇÃO MÉDIA DE TODOS OS VEÍCULOS
# ==============================================================================
# Propósito: Mostrar a tendência central de desvalorização para o mercado
#            representado no dataset.

plt.figure(figsize=(14, 8))
# Criamos o gráfico de linha sem o parâmetro 'hue'.
# O Seaborn irá automaticamente calcular a média de 'price' para cada 'vehicle_age'.
# A área sombreada (errorbar) representa o intervalo de confiança de 95% para a média.
sns.lineplot(data=base,
             x='vehicle_age',
             y='price',
             color='navy',      # Define uma cor única para a linha
             linewidth=3)
plt.title('Gráfico 8: Curva de Depreciação Média Geral do Mercado', fontsize=16)
plt.xlabel('Idade do Veículo (Anos)', fontsize=12)
plt.ylabel('Preço Médio (USD)', fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.savefig('8_curva_depreciacao_geral.png')
print("--> Gráfico 8 (curva_depreciacao_geral.png) salvo com sucesso!")

# ==============================================================================
# GRÁFICO 9: CURVA DE DEPRECIAÇÃO POR MARCA
# ==============================================================================
# Propósito: Contar uma história de negócio, comparando como as marcas
#            mais populares do dataset perdem valor ao longo do tempo.

# 1. Descobre quais são as 4 marcas mais comuns no dataset para a comparação
top_4_marcas = base['make'].value_counts().nlargest(4).index
#print(f"--> As 4 marcas mais comuns para a análise de depreciação são: {list(top_4_marcas)}")
# 2. Filtra o dataframe para conter apenas os dados dessas 4 marcas
df_top_marcas = base[base['make'].isin(top_4_marcas)]
# 3. Cria o gráfico de linhas, com uma linha para cada marca
plt.figure(figsize=(14, 8))
sns.lineplot(data=df_top_marcas,
             x='vehicle_age',
             y='price',
             hue='make',          # O 'hue' cria uma linha de cor diferente para cada 'make'
             errorbar=None,       # Remove a sombra de "intervalo de confiança" para um visual mais limpo
             linewidth=3)         # Deixa as linhas mais grossas
plt.title('Gráfico 9: Curva de Depreciação por Marca', fontsize=16)
plt.xlabel('Idade do Veículo (Anos)', fontsize=12)
plt.ylabel('Preço Médio (USD)', fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5) # Adiciona um grid para facilitar a leitura
plt.legend(title='Marca', fontsize=11)
plt.savefig('9_curva_depreciacao_marcas.png')
print("--> Gráfico 9 (curva_depreciacao_marcas.png) salvo com sucesso!")

# plt.show() # Descomente para mostrar os gráficos na tela