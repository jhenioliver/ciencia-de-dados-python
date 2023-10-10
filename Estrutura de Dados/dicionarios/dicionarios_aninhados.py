# dentro do dicionário "contatos", tem as chaves que são emails, e dentro dessas chvaes, está outro dicionário com chaves de nome e telefone
# síntaxe parecida com a de banco de dados

contatos = {
    "jheniffer@gmail.com": {"nome": "Jheniffer", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# acessando os dados:

# utilizando uma variável:

telefone = contatos["giovanna@gmail.com"]["telefone"]
print(telefone)

print("-" * 100)

# direto no print:

print(contatos["jheniffer@gmail.com"]["telefone"])

print(contatos["chappie@gmail.com"])

print("-" * 100)

# pode ter quantos dicionários aninhados quiser:

contatos02 = {
    "julia@gmail.com": {"nome": "julia", "telefone": "3334-4321", "extra": {"chave": 1}},
    "suzy@gmail.com": {"nome": "Suzy", "telefone": "3333-1234", "extra": {"chave": 10}}
}

print(contatos02["suzy@gmail.com"])

print(contatos02["suzy@gmail.com"]["extra"])

print(contatos02["suzy@gmail.com"]["extra"]["chave"])


