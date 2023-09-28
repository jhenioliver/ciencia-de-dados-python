saldo = 2000
saque = 500

#saque = int(input(f"Seu saldo é de {saldo}, quanto gostaria de sacar? \n"))

status = "Sucesso" if saldo >= saque else "Falha"
print(status)

# o status possui um if ternário:
# a primeira parte, anterior ao if ("sucesso") é o valor a ser retornado, caso a expressão do meio, pós o if e anterior ao else (saldo >= saque) seja verdadeira
# a útima parte, após o else ("falha") é o valor retornado caso a expressão do meio seja falsa.