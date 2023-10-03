nome = "Jheniffer de Oliveira"

# "sintaxe": [start:end:step]

print(nome[0])
# a primeira letra, o começo é sempre zero

print(nome[:9])
# se não indicar o start, automaticmanete é zero (o começo)

print(nome[10:])
# se não indicar o end, ele vao pegar até o fim da string

print(nome[10:21])
# indicando onde começa e termina

print(nome[10:21:2])
print(nome[:21:2])
# além do start e end, indica o step, emtão aqui vai pegar a cada duas letras

print(nome[:])
# vai mostrar uma cópia da string

print(nome[::-1])
# vai mostrar uma espelhamento da string

print(nome[-1])
# também pode ser utilizado números negativos