contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()

print(copia) # fez uma cópia do contatos

copia["guilherme@gmail.com"] = {"nome": "Gui"} # alterando o valores dessa cópia

print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}

print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}