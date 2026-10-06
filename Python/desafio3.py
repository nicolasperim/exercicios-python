def encontrar_maior(lista):
    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero
            pass
    return maior

numeros = []

quant = int(input("Quantos números serão digitados? "))
for i in range(quant):
    num = int(input(f"Digite o número {i + 1}º: "))
    numeros.append(num)

maior = encontrar_maior(numeros)

print(f"O maior número presente na lista é o {maior}")