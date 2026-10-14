def calcular_media(lista):
    return sum(lista) / len(lista)

notas = []

for i in range(3):
    nota = float(input(f"Digite a {i + 1}º nota: "))
    notas.append(nota)

media = calcular_media(notas)

print(f"Com a média de {media:.2f}, o aluno está", end=" ")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("De recuperação")
else:
    print("Reprovado")