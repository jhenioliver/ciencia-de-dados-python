# usando o método tuple:

letras = tuple("python") # só suporta um argumento, pois irá armazenar caractere por caractere (p-y-h-t-o-n)
print(letras)

# irá suportar mais de um argumento utilizando chaves:

palavras = tuple(["python", "declaração"])
print(palavras)

# declarando com parenteses:

frutas = ("maçã", "uva", "laranja",) # ATENÇÃO: adicionar uma vírgula ao final SEMPRE para evitar erros do interpretador
print(frutas)

# vírgula para reconhecer como tupla:

pais = ("Brasil",)
print(pais)