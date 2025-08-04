'''8. Análise de Notas de Turma
o Peça ao usuário a quantidade de alunos.
o Solicite as notas e calcule a média geral da turma, maior e menor nota'''

alunos = int(input("Digite a quantidade de alunos: "))
a = 1
soma = 0
maior = None
menor = None

while a <= alunos:
    nota = float(input(f"Digite a nota do aluno {a}: "))

    if a == 1:
        maior = nota
        menor = nota
    else:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
    soma += nota
    a += 1

media = soma / alunos

print(f"\nA média geral da turma é: {media:.2f}")
print(f"A maior nota da turma é: {maior}")
print(f"A menor nota da turma é: {menor}")