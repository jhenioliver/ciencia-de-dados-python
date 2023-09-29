# COM LISTA

frutas = ["limão", "uva"]

print("laranja" in frutas)
print("limão" in frutas)

print("uva" not in frutas) #utilizando o >not< in

# lembrando do case sensitive

print("Limão" in frutas) #não reconheceu porque o 'L' está em maiúsculo, diferente da declaração da variável que 'l' está em minúsculo

print("u" in frutas)

# COM CADEIA DE CARCATERES/STRING

curso = "Curso de Python"

print("Curso" in curso)
print("C" in curso) #reconheceu só a letra
print("curso" in curso) #não reconheceu pelo case sensitive no 'c' minúsculo

# COM INT

saques = [200, 450]

print(200 in saques)
print(2 in saques)