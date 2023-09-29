nome = input("insira seu nome: ")
sobrenome = input("insira seu sobrenome: ")

print(nome, sobrenome)

# com end | define o final do print
print(nome, sobrenome, end="... \n") # o \n é para pular uma linha

# com sep | define o separador, por padrão  é somente espaço
print(nome, sobrenome, sep="&") 

# com os dois
print(nome, sobrenome, sep="*", end="____ \n")