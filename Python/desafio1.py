def numero_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero_digitado = int(input("Digite um número: "))

if numero_par(numero_digitado):
    print(f"{numero_digitado} é um número PAR!")
else:
    print(f"{numero_digitado} é um número ÍMPAR!")