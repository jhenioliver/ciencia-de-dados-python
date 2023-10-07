""" 
Vai realizar uma cópia de uma lista já existente, porém essa cópia não será a mesma que a original e não terá vinculo com a original, então o que for alterado na cópia não será alterado na original
"""

lista1 = [1, "Python", [40, 30, 20]]

lista2 = lista1.copy() # copiando os valores da 1 para a 2

# a original e a cópia: 
print(lista1)
print(lista2)

print(id(lista1), id(lista2)) # possuem id's diferentes

# alterando algo na cópia:

lista2[0] = 2 # indicando que a posição zero agora recebe o valor 2 (antes era 1, como na original)

print(lista1)
print(lista2) # as alterações feitas na cópia não afetaram a original