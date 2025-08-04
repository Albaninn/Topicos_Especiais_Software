'''7. Gerador de Tabuada Personalizada
o Solicite um número e um intervalo (por exemplo, até 15).
o Exiba a tabuada do número até o limite informado.'''


numero = int(input("Digite um numero: "))
intervalo = int(input("Digite um intervalo: "))

i = 1

while i <= intervalo:
    print(numero, " X ",i, " = ", numero * i)
    i = i + 1