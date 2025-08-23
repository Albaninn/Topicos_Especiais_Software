produto = ("Livro", 59.90, 10)

print("Dados do produto: ", produto)

try:
    produto[1] = 49.90
except TypeError:
    print("Impossivel fazer alteraçao de tupla")