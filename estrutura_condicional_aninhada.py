tipo_conta = int(input(f"Digite o número correpondente ao seu tipo de conta: \n[1] Conta Normal \n[2] Conta Universitária \n"))
saldo = 1000

if tipo_conta == 1:
    conta_normal = True
    cheque_especial = 500
    saque = int(input(f"Seu saldo é de {saldo}, e você possui um cheque especial com valor de {cheque_especial}. \nQual o valor do saque? \n"))

elif tipo_conta == 2:
    conta_normal = False
    conta_universitaria = True
    saque = int(input(f"Seu saldo é de {saldo}. \nQual o valor do saque? \n"))
else:
    conta_normal, conta_universitaria = False, False
    print("Não foi possível identificar seu tipo de conta, verifique se digitou corretamente ou entre em contato com nosso suporte através do número XXXX-XXXX")

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif (saldo + cheque_especial) >= saque:
        print("Saque realizado com sucesso utilizando seu cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente.")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente.")

else:
    print("Não foi possível identificar seu tipo de conta, verifique se digitou corretamente ou entre em contato com nosso suporte através do número XXXX-XXXX")