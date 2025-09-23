import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter

# --- Preparação dos Dados (a mesma de antes) ---
# Substitua "titanic_train.csv" pelo caminho correto do seu arquivo se necessário
base = pd.read_csv("aula2209/titanic_train.csv")
base.columns = base.columns.str.strip().str.replace('\n', '')
base['Age'].fillna(base['Age'].median(), inplace=True)

# --- Criação do Gráfico com Facetas por Gênero ---
# Usamos displot para criar múltiplos gráficos
g = sns.displot(
    data=base,
    x='Age',
    hue='Survived',
    multiple='fill',
    col='Sex',  # <--- Esta é a grande novidade! Cria uma coluna de gráficos para cada gênero.
    bins=25,
    palette='coolwarm',
    height=6,   # Altura de cada gráfico
    aspect=1.2  # Proporção entre largura e altura
)

# --- Ajustes nos Títulos e Eixos ---
g.fig.suptitle('Proporção de Sobrevivência por Idade e Gênero', y=1.03, fontsize=16) # y=1.03 para não sobrepor os títulos
g.set_axis_labels('Idade', 'Percentual de Passageiros')
g.set_titles("Gênero: {col_name}") # Renomeia os títulos de cada subplot

# Ajusta a legenda
new_labels = ['Não Sobreviveu', 'Sobreviveu']
for t, l in zip(g._legend.texts, new_labels):
    t.set_text(l)

plt.show()