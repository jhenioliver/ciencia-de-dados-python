# vai ordenar a lista

linguagens = ["python", "js", "c", "java", "csharp"] # ordem por entrada
numeros = [5, 3, 2, 6, 1] # ordem por entrada

print(linguagens)
print(numeros)

# por padrão, ordena por ordem alfabética ou numérica
linguagens.sort() 
print(linguagens)

numeros.sort()
print(numeros)

#
print("--------------------------------------------")
#

# mas dentro do sort() pode indicar um argumento para a ordem:

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)