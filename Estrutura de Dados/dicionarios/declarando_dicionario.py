#utilizando chave
# síntaxe: nomedicionario = {"chave": valor, "chave": valor}

pessoa = {"nome": "Jheniffer", "idade": 18}
print(pessoa)

# utilizando a classe dict
# síntaxe: nomedicionario = dict(chave=valor, chave=valor)

pessoa = dict(nome="Jheniffer", idade=18)
print(pessoa)

# em todos, o "nome" e "idade" são a chave (valores imutáveis), e "Jheniffer" e 18 são os valores atribuídos


# atribuindo uma nova chave e um novo valor a um dicionário existente
# síntaxe: dicionario["chave"] = valor

pessoa["telefone"] = "3333-1234"
print(pessoa)