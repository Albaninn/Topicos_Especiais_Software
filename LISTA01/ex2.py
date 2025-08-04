
celsius = float(input("Insira a temperatura em Celsius: "))

# Fórmula para Kelvin: K = C + 273.15
kelvin = celsius + 273.15

# Fórmula para Fahrenheit: F = (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

print("\n--- Resultados da Conversão ---")

print(f"Celsius:    {celsius:.2f} °C")
print(f"Kelvin:     {kelvin:.2f} K")
print(f"Fahrenheit: {fahrenheit:.2f} °F")