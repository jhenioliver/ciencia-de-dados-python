MAIOR_IDADE = 18
IDADE_ESPECIAL = 12 #só de exemplo pra o elif

# apenas com o if

idade = int(input("informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("maior de idade, pode tirar a CNH.")
if idade < MAIOR_IDADE:
    print("ainda não pode tirar a CNH.")

# utilizando o else

idade = int(input("informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("maior de idade, pode tirar a CNH.")
else:
    print("ainda não pode tirar a CNH.")

# utilizando o elif

idade = int(input("informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("pode fazer aulas teóricas, mas não as práticas")
else:
    print("ainda não pode tirar a CNH")