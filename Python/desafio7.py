def contar_ocorrencias(lista_numeros, numero_procurado):
    contador = 0
    for numero in lista_numeros:
        if numero == numero_procurado:
            contador += 1
    return contador


# Programa Principal
valores_digitados = []

quantidade = int(input("Quantos valores vai adicionar à lista? "))
for i in range(quantidade):
    numero = int(input(f"Digite o {i + 1}° número: "))
    valores_digitados.append(numero)

num_escolhido = int(input("Por qual número você deseja procurar na lista? "))

total_ocorrencias = contar_ocorrencias(valores_digitados, num_escolhido)

print(
    f"O número {num_escolhido} foi encontrado {total_ocorrencias} vez(es) na lista."
)