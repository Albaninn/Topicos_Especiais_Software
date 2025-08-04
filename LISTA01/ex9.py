'''9. Verificador de Palíndromos
o Peça uma palavra ou frase.
o Verifique se é um palíndromo (lê-se igual de frente para trás).'''

frase = input("Digite uma palavra ou frase: ")

frase_limpa = frase.replace(" ", "").lower()

frase_invertida = frase_limpa[::-1]

if frase_limpa == frase_invertida:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")