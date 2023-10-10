contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# removendo o valor indicado:

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

# informando dois argumentos, caso a chave não exista, ele vai retornar o segundo argumento - que definimos como chaves {}

resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)