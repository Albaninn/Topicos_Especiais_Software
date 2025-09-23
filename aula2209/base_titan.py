import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter

# Carregando a base de dados a partir do arquivo enviado
base = pd.read_csv("aula2209/titanic_train.csv") # Removi o caminho do diretório local
base.columns = base.columns.str.strip().str.replace('\n', '')

# Preenche os valores nulos de 'Age' com a mediana
base['Age'].fillna(base['Age'].median(), inplace=True)

# Cria o histograma com proporções (percentual)
plt.figure(figsize=(12, 8))
ax = sns.histplot(data=base, x='Age', hue='Survived', multiple='fill', bins=30, palette='coolwarm', lw=0)

# Ajusta o eixo Y para mostrar em formato de porcentagem
ax.yaxis.set_major_formatter(PercentFormatter(1.0))

# --- Ajustes no Título e Legendas ---
ax.set_title('Proporção de Sobrevivência por Faixa Etária', fontsize=16)
ax.set_xlabel('Idade', fontsize=12)
ax.set_ylabel('Percentual de Passageiros', fontsize=12)

# O Seaborn pode criar a legenda automaticamente com 'hue', mas podemos customizá-la
# para garantir que os rótulos estejam corretos.
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, ['Não Sobreviveu', 'Sobreviveu'], title='Status')

plt.show()