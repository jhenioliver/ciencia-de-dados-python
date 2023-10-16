# chave=valor

def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# definindo o valor apenas colocando em ordem:

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

# utilizando chave=valor:

salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")

# utilizando dicionário (com **kwargs):

salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
