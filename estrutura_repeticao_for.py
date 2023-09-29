texto = input("insira um texto: ")
VOGAIS = "AEIOU"

for letra in texto: # a var letra está sendo criada agora para armazenar as letras do loop
    if letra.upper() in VOGAIS:
        print(letra, end=",") # printa as vogais, o end foi colocado apenas para as letras ficarem uma ao lado da outra com vírgula

# o else não é muito usado, mas ele vai ser adicionado após o loop
else:
    print() #só para pular uma linha do loop, já que o end anterior está sendo usada ENTRE as letras (por causa do loop)
    print("esse é o final do loop.")