def inverter_lista(lista_original):
    lista_inversa = []

    for n in range(len(lista_original) - 1, -1, -1):
        lista_inversa.append(lista_original[n])

    return lista_inversa

# Programa principal
lista = []
quantidade = int(input("Quantos números serão inseridos na lista? "))

for i in range(quantidade):
    numero = int(input(f"Digite o {i + 1}° valor: "))
    lista.append(numero)

nova_lista = inverter_lista(lista)

print(f"Lista original: {lista}")
print(f"Lista invertida: {nova_lista}")