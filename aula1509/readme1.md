# 1. Ler o arquivo CSV
base = pd.read_csv("forms2semestreup.csv")

# 2. Visualizar as primeiras linhas
print(base.head())

# 3. Visualizar as últimas linhas
print(base.tail())

# 4. Visualizar linhas aleatórias
print(base.sample(10))

# 5. Verificar quantidade de linhas e colunas
print(base.shape)

# 6. Conferir os nomes das colunas
print(base.columns)

# 7. Verificar os tipos de dados
print(base.dtypes)

# 8. Informações gerais sobre a base
print(base.info())

# 9. Estatísticas descritivas de todas as colunas
print(base.describe(include="all"))

# 10. Conferir valores ausentes por coluna
print(base.isnull().sum())

# 11. Conferir registros duplicados
print(base.duplicated().sum())

# 12. Contar valores únicos em cada coluna
print(base.nunique())

# 13. Selecionar somente colunas numéricas
dados_numericos = base.select_dtypes(include=["int64", "float64"])
print(dados_numericos.head())

# 14. Selecionar somente colunas categóricas
dados_categoricos = base.select_dtypes(include=["object", "category", "bool"])
print(dados_categoricos.head())

# 15. Exibir as 5 primeiras linhas e 5 primeiras colunas
print(base.iloc[:5, :5])

# 16. Exibir apenas as 5 primeiras colunas
print(base.iloc[:, :5])

# 17. Exibir apenas as 10 primeiras linhas
print(base.iloc[:10, :])

# 18. Selecionar uma coluna específica
print(base["coluna_exemplo"].head())

# 19. Contar frequências de uma coluna
print(base["coluna_exemplo"].value_counts())

# 20. Ver valores únicos de uma coluna
print(base["coluna_exemplo"].unique())

# 21. Ordenar registros por uma coluna (crescente)
print(base.sort_values("coluna_exemplo").head())

# 22. Ordenar registros por uma coluna (decrescente)
print(base.sort_values("coluna_exemplo", ascending=False).head())

# 23. Calcular matriz de correlação
print(dados_numericos.corr())

# 24. Visualizar apenas a correlação com uma coluna específica
print(dados_numericos.corr()["Nota_Final"].sort_values(ascending=False))

# 25. Calcular médias de todas as colunas numéricas
print(base.mean(numeric_only=True))

# 26. Calcular medianas de todas as colunas numéricas
print(base.median(numeric_only=True))

# 27. Calcular moda de todas as colunas
print(base.mode().head())

# 28. Calcular mínimos de todas as colunas numéricas
print(base.min(numeric_only=True))

# 29. Calcular máximos de todas as colunas numéricas
print(base.max(numeric_only=True))

# 30. Calcular desvio padrão de todas as colunas numéricas
print(base.std(numeric_only=True))

# 31. Calcular variância de todas as colunas numéricas
print(base.var(numeric_only=True))

# 32. Criar nova coluna a partir de cálculo simples
base["Nova_Coluna"] = 2025 - base["coluna_exemplo_numerica"]
print(base.head())

# 33. Remover linhas com valores ausentes
print(base.dropna().head())

# 34. Substituir valores ausentes por 0
print(base.fillna(0).head())

# 35. Filtrar registros por condição (> 10)
print(base.query("coluna_exemplo > 10").head())

# 36. Filtrar registros por igualdade
print(base.query("coluna_exemplo == 'categoria'").head())

# 37. Agrupar por coluna categórica e calcular médias
print(base.groupby("coluna_exemplo").mean(numeric_only=True))

# 38. Agrupar por coluna categórica e contar registros
print(base.groupby("coluna_exemplo").count())

# 39. Calcular correlação com Pearson
print(dados_numericos.corr(method="pearson"))

# 40. Calcular correlação com Kendall
print(dados_numericos.corr(method="kendall"))

# 41. Calcular correlação com Spearman
print(dados_numericos.corr(method="spearman"))