def remover_duplicados(lista_original):
    nova_lista = []
    for item in lista_original:
        if item not in nova_lista:
            nova_lista.append(item)
    return nova_lista

# Programa principal
lista = []

quantidade = int(input("Quantos números terão na lista? "))

for i in range(quantidade):
    numero = int(input(f"Digite o {i + 1}° valor: "))
    lista.append(numero)

duplicata = remover_duplicados(lista)

print(f"Lista sem alterações: {lista}")
print(f"Lista sem duplicatas: {duplicata}")