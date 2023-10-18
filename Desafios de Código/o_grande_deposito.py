valor = float(input())

if valor > 0:
  saldo_atual = valor
  print(f"""Deposito realizado com sucesso! 
  Saldo atual: R$ {saldo_atual:.2f}""")
elif valor == 0:
  saldo_atual = valor
  print("Encerrando o programa...")
else:
  print("Valor invalido! Digite um valor maior que zero.")