# somente "copiando" a lista:
numeros = [1, 2, 30, 21, 9, 65, 34]
pares = [numero for numero in numeros]
print(pares)
print(numeros)

#
print("-------------------------")
#

# adicionando filtro/função

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
print(numeros)

#
print("-------------------------")
#

# modificando valor

quadrado = [numero ** 2 for numero in numeros]
print(quadrado)