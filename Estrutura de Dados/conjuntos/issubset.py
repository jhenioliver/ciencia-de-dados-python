# se está dentro do conjunto

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # se o conjunto a está dentro de b - true
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  # se b está dentro de a - false
print(resultado)