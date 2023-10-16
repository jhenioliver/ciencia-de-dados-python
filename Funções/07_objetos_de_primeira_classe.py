def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

"""
normalmente seria feito assim:

print(somar(10, 10))
print(subtrair(10,10))

"""

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")


exibir_resultado(10, 10, somar)  # a palavra "somar" vai ir em 'função', fazendo que a função somar seja executada dentro da variável resultado
exibir_resultado(10, 10, subtrair)

# utilizando em variáveis também:

operacao = somar

print(operacao(2, 5))