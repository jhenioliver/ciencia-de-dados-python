# Operador AND - para ser true, TUDO precisa ser true/verdadeiro | basta um falso para dar false

print(True and True)
print(True and False)
print(False and False)

# Operador OR - para ser true, basta apenas UMA ser true/verdadeira | precisa todos falsos para dar false

print(True or True)
print(True or False)
print(False or False)

# Exemplo

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp_1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp_1)

# Para facilitar e melhorar as expressões lógicas, é recomendado a convenção dos parenteses ():

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

# Outra dica, é não criar linhas de expressões/comprações muito longas - geralmente elas podem ser quebradas ou divididas em variáveis
# Quebrando o exemplo anterior:

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)

