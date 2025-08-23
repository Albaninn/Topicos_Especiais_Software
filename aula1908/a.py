'''s1 = "Ele disse: 'Oi'"
s2 = 'Ela respondeu: "Olá"'
s3 = "Ele disse: \"Oi\""

print(s1)
print(s2)
print(s3)

print("Data" + "Science")
print("ha" * 3)
print("Py" in "Python")
print("Py" in "python")
print("java" not in "Python")

print(len("casa"))

print(ord("A"))
print(ord("ç"))

print(chr(65))
print(chr(231))

print(ord("L"))
print(ord("u"))
print(ord("c"))
print(ord("a"))
print(ord("s"))

print("python".upper())
print("python".lower())
print("python".capitalize())
print("curso de pyhton".title())


s = "banana maçã uva banana abacaxi banana"
print(s.count("banana"))
print(s.find("maçã"))
print(s.rfind("banana"))
print(s.startswith("banana"))
print(s.endswith("banana"))

frase = "Ordem e Progresso"

print(frase.replace("e", "&&"))

palavra = frase.split()
print(palavra)

itens = ["a", "b", "c"]
print(" | ".join(itens))

nome = "Lucas"
idade = 24
aniversario = "17/05"

print(f"{nome} fez {idade} anos dia {aniversario}")

curso = "BSI"

dur_total = 4
dur_atual = 4
dur_final = dur_total - dur_atual

print(
    f"{nome} está cursando {curso}. "
    f"O curso tem a duraçao de {dur_total} anos"
    f"e atualmente ele está no {dur_atual}º ano "
)

texto = "Relatório"

print(f"{texto:-^20}")
print(f"{texto:.^20}")
print(f"{texto:.<20}")
print(f"{texto:.>20}")'''

texto1 = "Produto"
texto2 = "Preço"

produto1 = input("Insira o produto: ")
preço1 = float(input("O valor:"))
produto2 = input("Insira o produto: ")
preço2 = float(input("O valor:"))
produto3 = input("Insira o produto: ")
preço3 = float(input("O valor:"))

print
print(f"{texto1: <12} {texto2: >9}")
print("-"*22)
print(f"{produto1:<12} R$ {preço1:>6.2f}")
print(f"{produto2:<12} R$ {preço2:>6.2f}")
print(f"{produto3:<12} R$ {preço3:>6.2f}")
