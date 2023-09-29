"""for numero in range(10):

    if numero == 5:
        continue

    print(numero, end=" ")"""
# o continue vai pular aquilo que for sua condição - aqui a condição ser == 5, então na listagem ele pula o 5 e continua o range
# diferente do break, que encerra tudo, o continue apenas "pula/ignora"

# também pode ser utilizado no while, mas sempre lembrar de definir um break válido para não ser um laço infinito

while True:
    numero = int(input("informe um número: "))

    if numero == 10: #se o num. for 10, vai parar
        break

    if numero % 2 == 0: #se o num. for par, ele pula e não exibe o print
        continue

    print(numero) 