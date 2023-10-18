valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

while periodo > 0:
    periodo -= 1
    juros = valor_inicial * taxa_juros
    valor_inicial += juros

valor_final = valor_inicial
print(f"Valor final do investimento: R$ {valor_final:.2f}")