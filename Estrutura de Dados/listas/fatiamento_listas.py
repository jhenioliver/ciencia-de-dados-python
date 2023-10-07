lista = ["p", "y", "t", "h", "o", "n"]

# lembrando que a contagem começa no zero, e o último número é exclusivo (não vai aparecer)

# indicando apenas onde começa
print(lista[2:])

# indicando apenas onde termina
print(lista[:2])

# indicando de qual começa e em qual termina
print(lista[1:3])

# indicando de qual começa, termina e como deve ser a sequência/os passos (no exemplo, vai andar de 2 em 2)
print(lista[0:3:2])

# sem indicar nada, vai ir do começo ao fim de toda a string (pode ser com um : ou dois :)
print(lista[::])

# espelhamento

print(lista[::-1])