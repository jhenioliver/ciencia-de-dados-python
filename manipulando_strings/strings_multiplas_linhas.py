nome = "Jheniffer"

# para ter múltiplas linhas basta informar três aspas simples ou duplas na atribuição

mensagem = f"""Olá! Tudo bem?
Meu nome é {nome}."""

print(mensagem)

mensagem = """Essa mensagem tem diferentes
recuos e        espaços
    esse recuos e  e s p a ç o s
        constam na string 
                        final"""

print(mensagem)

# pode ser utilizado direto no print também

print(""" 
    =============== MENU ================

    1 - Depositar
    2 - Sacar
    0 - Sair

    =====================================

        Obrigado por utilizar nosso sistema!
""")