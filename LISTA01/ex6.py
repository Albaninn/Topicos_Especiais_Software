'''6. Caixa Eletrônico Simples
o Simule saques de um caixa eletrônico.
o O programa deve solicitar o valor do saque e calcular a quantidade de cédulas de 100, 50, 20
e 10 necessárias'''

valor_str = input("Digite o valor que deseja sacar: R$ ")

if valor_str.isdigit():
    valor_saque = int(valor_str)

    if valor_saque % 10 != 0:
        print("Erro: O valor do saque deve ser múltiplo de R$10.")
    else:
        valor_restante = valor_saque

        cedulas_100 = valor_restante // 100
        valor_restante = valor_restante % 100

        cedulas_50 = valor_restante // 50
        valor_restante = valor_restante % 50

        cedulas_20 = valor_restante // 20
        valor_restante = valor_restante % 20

        cedulas_10 = valor_restante // 10

        print("\\nPara sacar R$", valor_saque, "você receberá:")
        
        if cedulas_100 > 0:
            print(cedulas_100, "cédula(s) de R$ 100")
        if cedulas_50 > 0:
            print(cedulas_50, "cédula(s) de R$ 50")
        if cedulas_20 > 0:
            print(cedulas_20, "cédula(s) de R$ 20")
        if cedulas_10 > 0:
            print(cedulas_10, "cédula(s) de R$ 10")
else:
    print("Erro: Por favor, digite um número inteiro válido.")