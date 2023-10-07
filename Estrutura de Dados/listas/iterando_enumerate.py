# iterando com for

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

# utilizando enumerate

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")