opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n>"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
    elif (opcao != 1 and opcao !=0) or (opcao != 2 and opcao != 0):
        print("Insira um número válido.")

else:
    print("Obrigado por utilizar nosso sistema!")