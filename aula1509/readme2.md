import pandas as pd
from datetime import datetime

# 1. Ler o arquivo CSV
base = pd.read_csv("forms2semestreup.csv")

# 2. Garantir que a coluna de data esteja em datetime
#    Ajuste o nome da coluna se necessário, por exemplo "data_nascimento" ou "nascimento"
base["Data_Nascimento"] = pd.to_datetime(base["Data_Nascimento"], errors="coerce", dayfirst=True)

# 3. Conferir quantas datas inválidas ficaram como NaT
print(base["Data_Nascimento"].isna().sum())

# 4. Definir uma data de referência para o cálculo de idade
#    Use a data atual ou fixe uma data para reprodutibilidade
data_referencia = pd.Timestamp("2025-09-15")

# 5. Calcular idade inteira em anos completos
base["Idade"] = (
    data_referencia.year
    - base["Data_Nascimento"].dt.year
    - ((data_referencia.month, data_referencia.day) < (base["Data_Nascimento"].dt.month, base["Data_Nascimento"].dt.day))
).astype("Int64")

# 6. Ver as primeiras linhas com a nova coluna
print(base[["Data_Nascimento", "Idade"]].head())

# 7. Ordenar pela idade em ordem crescente
print(base.sort_values("Idade").head(10))

# 8. Ordenar pela idade em ordem decrescente
print(base.sort_values("Idade", ascending=False).head(10))

# 9. Selecionar apenas registros com idade válida
apenas_idade_valida = base[base["Idade"].notna()]
print(apenas_idade_valida.shape)

# 10. Converter a coluna Idade para numérica inteira padronizada quando possível
base["Idade"] = pd.to_numeric(base["Idade"], errors="coerce").astype("Int64")
print(base["Idade"].dtype)

# 11. Separar subconjunto de dados contendo somente a coluna Idade
dados_so_idade = base[["Idade"]]
print(dados_so_idade.head())

# 12. Separar colunas numéricas incluindo Idade
dados_numericos = base.select_dtypes(include=["int64", "float64", "Int64"])
print(dados_numericos.head())

# 13. Resumo estatístico da idade
print(base["Idade"].describe())

# 14. Criar faixas etárias com pd.cut
faixas = [0, 12, 17, 24, 34, 44, 59, 120]
rotulos = ["0_12", "13_17", "18_24", "25_34", "35_44", "45_59", "60_120"]
base["Faixa_Etaria"] = pd.cut(base["Idade"], bins=faixas, labels=rotulos, right=True, include_lowest=True)
print(base[["Idade", "Faixa_Etaria"]].head(15))

# 15. Contagem por faixa etária
print(base["Faixa_Etaria"].value_counts(dropna=False))

# 16. Agrupar por faixa etária e calcular médias das colunas numéricas
print(base.groupby("Faixa_Etaria").mean(numeric_only=True))

# 17. Extrair componentes de data a partir de Data_Nascimento
base["Ano_Nasc"] = base["Data_Nascimento"].dt.year
base["Mes_Nasc"] = base["Data_Nascimento"].dt.month
base["Dia_Nasc"] = base["Data_Nascimento"].dt.day
print(base[["Data_Nascimento", "Ano_Nasc", "Mes_Nasc", "Dia_Nasc"]].head())

# 18. Verificar cardinalidade de Faixa_Etaria e Idade
print(base["Faixa_Etaria"].nunique())
print(base["Idade"].nunique())

# 19. Amostra aleatória para inspeção manual do cálculo
print(base[["Data_Nascimento", "Idade", "Faixa_Etaria"]].sample(10, random_state=42))

# 20. Exportar um recorte contendo identificador, Data_Nascimento e Idade
#     Ajuste o nome da coluna identificadora conforme existir na base
colunas_exportar = [c for c in ["ID", "Nome", "Data_Nascimento", "Idade", "Faixa_Etaria"] if c in base.columns]
base[colunas_exportar].to_csv("idade_calculada.csv", index=False)