contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# se procurar normalmente pela chave, e ela não existir, irá exibir um erro e parar o código:

# contatos["chave"]  # KeyError

# para evitar esse erro, utiliza-se o método get - ele vai verificar se a chave existe e te retornar um valor.

# colocando apenas a suposta chave:

resultado = contatos.get("chave")  # None
print(resultado)

# informando dois argumentos (se chave nao existir, me retorne um dicionário vazio):

resultado = contatos.get("chave", {})  # {}
print(resultado)

# quando a chave existe:

resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)