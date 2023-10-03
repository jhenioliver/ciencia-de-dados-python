# maiúscula, minúscula e título

nome = "jHeNIfFeR"

print(nome.upper()) # MAIÚSCULA
print(nome.lower()) # minúscula
print(nome.title()) # Título

# removendo espaços

curso = "   Python     "

print(curso + ".") # com os espaços
print(curso.strip() + ".") # remove o espaço dos dois lados
print(curso.lstrip() + ".") # remove somente da esquerda
print(curso.rstrip() + ".") # remove somente da direita

# centralização

menu = "Centro"

print(menu.center(10, "#")) 
print(menu.center(10)) # o segundo argumento é opcional, o python adiciona um espaço no lugar

# junção

print("-".join(menu))
print("*".join(menu))