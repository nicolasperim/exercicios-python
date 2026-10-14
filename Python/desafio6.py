def filtrar_pares(lista_numeros):
    pares = []

    for n in lista_numeros:
        if n % 2 == 0:
            pares.append(n)
    return pares
    
numeros_inteiros = []

quantidade_lista = int(input("Quantos números terão na lista? "))

for i in range(quantidade_lista):
    numeros = int(input(f"Digite o {i + 1}° número: "))
    numeros_inteiros.append(numeros)

lista_pares = filtrar_pares(numeros_inteiros)

print(f"Lista original: {numeros_inteiros}")
print(f"Apenas os pares: {lista_pares}")