linguagens = ["python", "js", "c"]

print(linguagens) # objetos que foram declarados

linguagens.extend(["java", "csharp"]) # adicionando mais objetos à mesma lista

print(linguagens) # adicionou e juntou os novos objetos com os que já estavam - diferente do append

# ele não mescla, apenas coloca os novos objetos ao final da lista
# isso faz com que não reconheça valores repetidos:

linguagens.extend(["python"])

print(linguagens)