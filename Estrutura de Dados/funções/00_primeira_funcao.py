# declaração:

# síntaxe : def nome_identificador (argumento_opcional)

def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!") # argumento SEM atribuição de valor na declaração


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!") # argumento COM declaração de valor na atribuição


# execução

exibir_mensagem()
exibir_mensagem_2(nome="Guilherme") # como não tinha sido atribúido valor no argumento anteriormente, é necessário atribuir aqui
exibir_mensagem_3() # já foi atribuído valor na declaração
exibir_mensagem_3(nome="Chappie") # mas podemos atribuir novamente outro valor
