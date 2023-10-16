""" 
síntaxe: posicao_apenas1, posicap_apenas2, /, posicao_ou_nome, *, nome_apenas1, nome_apenas2

 antes da barra /, tudo precisa ser definido APENAS por POSIÇÃO

 depois da barra / até o asterisco *, pode ser definido OU por nome OU por posição (você escolhe, mas não pode misturar)

 depois do asterisco *, tudo precisa ser definido APENAS por NOME (chave=valor)

"""


def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# ou seja: modelo, ano e placa precisam ser definidos por posição
# e marca, moto e combustível podem ser ou por posição ou por nome

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

# o exemplo abaixo dá erro, por definir modelo, ano e placa por nome ao invés de posição:

# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido