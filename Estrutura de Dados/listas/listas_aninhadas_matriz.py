# é possível colocar listas dentro de uma lista, criando uma "matriz" (onde podemos percorrer as linhas/listas)

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # vai retornar a primeira lista/linha
print(matriz[0][0])  # retorna o primeiro valor da primeira lista/linha
print(matriz[0][-1])  # retorna o último valor da primeira lista/linha
print(matriz[-1][-1])  # retorna o último valor da última lista/linha 