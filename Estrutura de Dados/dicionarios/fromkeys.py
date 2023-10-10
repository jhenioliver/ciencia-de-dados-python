# criando apenas as chaves, sem agregar nenhum valor à elas:

resultado = dict.fromkeys(["nome", "telefone"])
print(resultado)

# criando as chaves e adicionando um mesmo valor para todas elas de uma só vez:

resultado = dict.fromkeys(["nome", "telefone"], "valor")
print(resultado)

# se for usar um dicionário existente, basta substituir o "dict" pelo nome do dicionário