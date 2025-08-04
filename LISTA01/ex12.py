'''12. Um sistema recebe dados do usuário sempre em formato de texto (string). Para cálculos, é
necessário converter os valores para números decimais.
Pede-se
• Crie um código que solicite dois valores decimais e exiba a média entre eles.
• Explique teoricamente:
1. Por que é necessário usar a função float() no input()?
R: É necessario para converter o formato da entrada de dado
2. O que aconteceria se fosse feita a soma de duas strings ao invés de dois números?
R: Nao seria feita a soma, apenas agregado uma string no final da outra'''


valor1 = float(input("Digite o valor 1: "))
valor2 = float(input("Digite o valor 2: "))

media = (valor1 + valor2)/2

print("A média entre esses valores é de: ", media)