import pandas as pd
import matplotlib.pyplot as plt # Importa para criar gráficos
import seaborn as sns          # Importa para gráficos mais bonitos

pd.set_option('display.max_columns', None)

base = pd.read_csv("aula1509/forms2semestreup.csv")
base.columns = base.columns.str.strip().str.replace('\n', '')

base['DATA DE NASCIMENTO'] = pd.to_datetime(base['DATA DE NASCIMENTO'], errors='coerce', dayfirst=True)
base.dropna(subset=['DATA DE NASCIMENTO'], inplace=True)

base['IDADE'] = (pd.Timestamp.now() - base['DATA DE NASCIMENTO']).dt.days / 365.25
base['IDADE'] = base['IDADE'].astype(int)

coluna_trabalho = 'Você possui trabalho ou estágio atualmente?'

mapa_trabalho = {
    'Trabalho/estágio período integral (8 horas ou mais por dia)': 1,
    'Trabalho/estágio meio período (até 6 horas por dia)': 1,
    'Trabalho informal ou esporádico': 1,
    'Não trabalho nem faço estágio': 0
}
base[coluna_trabalho] = base[coluna_trabalho].map(mapa_trabalho)

base.dropna(subset=[coluna_trabalho], inplace=True)

analise_final = base.groupby(coluna_trabalho)['IDADE'].describe()

print("Análise de Idade vs. Trabalho/Estágio (0 = Não, 1 = Sim):")
print(analise_final)

base['STATUS_TRABALHO'] = base[coluna_trabalho].map({0: 'Não Trabalha/Estagia', 1: 'Trabalha/Estagia'})

plt.figure(figsize=(8, 6))
sns.boxplot(x='STATUS_TRABALHO', y='IDADE', data=base)

plt.title('Distribuição da Idade por Status de Trabalho/Estágio')
plt.xlabel('Status de Trabalho/Estágio')
plt.ylabel('Idade')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()