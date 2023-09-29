# função built-in range com o comando for:

for numero in range(0, 11):
    print(numero, end=" ")

# poderia ser também: range(0, 11) - porém como sempre começa do zero, não é especificamente necessário
# lembrando que o número final é exclusivo - não irá ser exibido

##

# tabuada do 5:

for numero in range(0, 51, 5):
    print(numero)

# em range(), o primeiro número (0) é de onde começa, o do meio é onde vai parar (51), e o último é de quanto em quanto vai ser somado (5)