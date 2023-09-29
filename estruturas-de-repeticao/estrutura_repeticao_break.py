# exemplo de break no while

while True:
    numero = int(input("informe um número: "))

    if numero == 10:
        break

    print(numero) 
# o break corta o laço de repetição quando sua condição for atendida - aqui, será cortado ao receber 10

# exemplo de break no for

for numero in range(100):

    if numero == 10:
        break

    print(numero)
# com o range, o normal seria ele ir até 100, porém o break vai parar a contagem em 9 (porque o 10 é exclusivo em break por ser o último número)