'''11. Um professor decidiu que a nota mínima para aprovação será 6.0. Porém, se o aluno tiver frequência
inferior a 75%, ele será reprovado, mesmo que a nota seja maior que 6.
Pede-se
• Desenvolva um código em Python que leia a nota e a frequência (%) do aluno e exiba se ele foi
aprovado ou reprovado.
• Explique teoricamente:
1. Por que o uso do operador lógico and é necessário nessa situação?
R: Ele é necessario pois são duas variaveis juntas para ter a resposta
2. O que aconteceria se fosse usado or no lugar de and?
R: Caso usassemos or ele iria contar apenas uma das duas variaveis, por exemplo, se o aluno tem apenas frequancia mas nao nota suficiente'''



nota = float(input("Digite a nota do aluno: "))
freq = float(input("Digite a frequencia (em %): "))

if nota >= 6 and freq >= 75:
    print("Aprovado")
else:
    print("Reprovado")
