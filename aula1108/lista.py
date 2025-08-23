nomes = ["lucas","matheus","pedro","marco","joao"]
print("Lista  inicial de nomes: ")
for nome in nomes:
    print(f"- {nome}")
print("Cadastre novos nomes: ")
i = 0
while i < 5:
    nomes.append(input(f"Digite o {i+1}º nome: "))
    i += 1
print("\nA lista completa dos nomes cadastrados: ")
print(nomes)
for indice in range(len(nomes)):
    print(f"O item '{nomes[indice]}' está na sequencia {indice+1}.")