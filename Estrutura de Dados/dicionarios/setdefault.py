contato = {"nome": "Guilherme", "telefone": "3333-2221"}

# se a chave estiver sem valor, vai definir esse valor indicado a ela, se não, o valor permanece o mesmo:

contato.setdefault("nome", "Giovanna")  # se a chave 'nome' estiver vazia, atribua o valor como "Giovanna"
print(contato)  # como a chave tinha o valor "Guilherme", esse valor permaneceu o mesmo

contato.setdefault("idade", 28)  # se a chave 'idade' estiver vazia, definir como 28
print(contato)  # como a chave nem sequer existia, ela foi criada e atribuído o valor 28