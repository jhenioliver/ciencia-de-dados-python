nome = "Jheniffer"
idade = 18
profissao = "Programadora"
saldo = 45.582

dados = {"nome": "Jheniffer", "idade": 18} #dicionário de dados

# old style

print("nome: %s idade: %d" % (nome, idade))

# format

print("nome: {} idade: {}".format(nome, idade))

print("nome: {0} idade: {1} nome2: {0} profissão: {2}".format(nome, idade, profissao)) 
#colocando a ordem das variáveis, assim podendo repetir a mesma

print("nome: {nome} idade: {age}".format(nome=nome, age=idade)) 
#precisa indicar uma variável para cada nome dado entre chaves

print("nome: {nome} idade: {idade}".format(**dados))
#vai buscar as variáveis no dicionário de dados que criamos (dados)

# f-string

print(f"nome: {nome} idade: {idade}")

#formatando f-string

print(f"saldo: {saldo}")

print(f"Saldo: {saldo:.2f}") #vai pegar só duas casas depois da vírgula
print(f"Saldo: {saldo:10.2f}")