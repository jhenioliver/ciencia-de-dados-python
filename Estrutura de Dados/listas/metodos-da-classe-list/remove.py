# vai remover um objeto da lista
# precisa indicar o nome do objeto (e não o índice)

linguagens = ["python", "js", "c", "java", "csharp", "java"]
print(linguagens)

linguagens.remove("c")
print(linguagens)

# se houver mais de uma vez o argumento, ele repetido, será eliminado o primeiro que aparecer na ordem

linguagens.remove("java")
print(linguagens) # removeu só o primeiro