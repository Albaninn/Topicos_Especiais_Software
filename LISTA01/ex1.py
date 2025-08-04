'''print("Hello World")

print(1500+(1500*5/100))'''

nome = input("Qual seu nome: ")
print(f"\nOlá, {nome}!")

nota1 = 0
nota2 = 0

while not (0 < nota1 <= 10) or not (0 < nota2 <= 10):
    print("As notas devem estar entre 0 e 10.")
    nota1 = float(input("Digite sua nota 1: "))
    nota2 = float(input("Digite sua nota 2: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print(f"Parabéns {nome}, você foi aprovado com média {media:.2f}!")
else:

    print(f"{nome}, infelizmente você foi reprovado com média {media:.2f}.")
