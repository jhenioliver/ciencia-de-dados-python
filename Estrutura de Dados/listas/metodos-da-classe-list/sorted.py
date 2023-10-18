# assim como o sort, também serve para ordenar e pode receber argumentos
# porém, ele trabalha com outras formas que não são listas

linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens)) # ORDEM ALFABÉTICA
print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]