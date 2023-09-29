def sacar(valor): #início do bloco do método
    saldo = 500
    if saldo >= valor: #início do bloco do if
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    print("obrigado por ser nosso cliente, tenha um bom dia!")

sacar(100)

# Anotações
"""

Para iniciar um bloco, utiliza o caractere de dois pontos :
    Então temos o bloco do método e o bloco do if
A cada novo bloc, precisa adicionar 4 novos espaços em brancos, ou 1 tab que equivale aos 4 espaços
    Por exemplo, após o início do bloco do método, tudo que está dentro dele possui 1 tab em branco
        Sinalizando que o saldo e o if fazem parte do método
    E quando abrimos o bloco if, colocamos + 1 tab em branco, sinalizando que os prints fazem parte do if

    o último print está fora do if, pois só tem 1 tab em branco, está dentro do bloco do método
        logo, ele não depende da validação do if para ser exibido na tela
        para testar, basta colocar um valor maior que o saldo em sacar(), que a mensagem será exibida
        mesmo sendo maior que o saldo, pois ele não passa pelo if, diferente dos primeiros prints que precisam da validação do if

"""