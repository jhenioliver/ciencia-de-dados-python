# os conjuntos não possuem objetos repetidos - usados para eliminar itens duplicados
    # e eles não trazem o resultado em ordem
# há diferentes formas de declarar:

# parecido com lista/tupla:

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)

# caractere por caractere:
letras = set("abacaxi")
print(letras)

# dois parenteses

carros = set(("palio", "gol", "celta", "palio"))
print(carros)

# só com chaves (não precisa do "set")
linguagens = {"python", "java", "python"}
print(linguagens)