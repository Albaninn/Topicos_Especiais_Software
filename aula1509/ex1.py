import pandas as pd

base = pd.read_csv(r"aula1509\alunos.csv")

print(base.head())

print(base.iloc[:,:5])
