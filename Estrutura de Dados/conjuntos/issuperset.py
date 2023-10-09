# se o conjunto está dentro do outro, mas com síntaxe diferente

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # se b está em a - False
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # se a está dentro de b - True
print(resultado)