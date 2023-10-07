# utilizado para adicionar UM valor/objeto na lista - sem mesclar com os valores existentes

linguagens = []

# síntaxe: nomedalista.append(valor a ser add)

linguagens.append("python")
linguagens.append("js")
linguagens.append("c")

print(linguagens)

# ele NÂO junta os novos valores que são adicionados - diferente do extend

linguagens.append(["java", "csharp"])

print(linguagens)