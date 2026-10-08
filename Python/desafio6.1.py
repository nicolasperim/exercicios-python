def filtrar_maiores_que_dez(lista_numeros):
    numeros_filtrados = []
    for numero in lista_numeros:
        if numero > 10:
            numeros_filtrados.append(numero)
    return numeros_filtrados

valores_digitados = []
quantidade = int(input("Digite a quantidade de números que vai inserir: "))

for i in range(quantidade):
    numero = int(input(f"Digite o {i + 1}° número: "))
    valores_digitados.append(numero)

maiores_que_dez = filtrar_maiores_que_dez(valores_digitados)

print(f"A lista completa: {valores_digitados}")
print(f"Apenas os números maiores que 10: {maiores_que_dez}")