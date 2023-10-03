produto_1 = 20
produto_2 = 10

#operações básicas
print("operações básicas: ")
print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)

#módulo (resto da divisão)
print("módulo: ")
print(produto_1 % produto_2)

#exponenciação
print("exponenciação: ")
print(produto_1 ** produto_2)

#testando precedência de operações
print("precedência: ")
print(produto_1 + produto_2 * 2)

x = 10 + 5 * 4
print(x)

x = (10 + 5) * 4
print (x)


y = 10 / 2 + 25 * 2 - 2 ** 2
print(y)

#o python executa perfeitamente o cálculo acima, porém, ao olho humano pode demorar um pouco para compreender a conta e a ordem
#então por boa prática, podemos facilitar a visualização com parenteses ()
#os parenteses () podem servir para alterar a ordem de precedência, ou para facilitar o entendimento:

y = (10 / 2) + (25 * 2) - (2 ** 2)
print(y)

# o resultado é o mesmo pois não alteramos a precedência, mas melhorou a visualização da conta

#alterando a precedência:

y = (10 / 2) + (25 * (2 - 2) ** 2)
print(y)

y = (10 / (2 + 25) * 2) - (2 ** 2)
print(y)