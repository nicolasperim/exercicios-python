def contagem_regressiva(inicio):
    for i in range(inicio, -1, -1):
        print(i)

numero = int(input("Digite um número inteiro: "))
contagem_regressiva(numero)
print("Fim da contagem.")