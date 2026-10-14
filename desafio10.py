def encontrar_segundo_maior(lista_numeros):
    maior = lista_numeros[0]
    segundo_maior = lista_numeros[0]

    for n in lista_numeros:
        if n > maior:
            segundo_maior = maior
            maior = n
        elif n > segundo_maior and n != maior:
            segundo_maior = n

    return segundo_maior


# Programa Principal
lista = []

quantidade = int(input("Digite a quantidade de números que terão na lista: "))
for i in range(quantidade):
    numero = int(input(f"Digite o {i + 1}° número: "))
    lista.append(numero)

segundo = encontrar_segundo_maior(lista)

print(
    f"O maior número presente na lista é {max(lista)} e o segundo maior é {segundo}"
)