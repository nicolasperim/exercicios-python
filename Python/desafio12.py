# Sistema de Cadastro de Alunos com Dicionários e Listas

turma = []

while True:
    aluno = {}
    aluno["nome"] = input("Nome do aluno: ")

    # Validação da nota
    while True:
        aluno["nota"] = float(input(f"Nota do {aluno['nome']}: "))
        if 0 <= aluno["nota"] <= 10:
            break
        print("❌ Nota inválida. A nota deve ser entre 0 e 10.")

    turma.append(aluno)

    # Validação para continuar
    continuar = input("Deseja adicionar mais alunos? [S/N]: ").strip().lower()[0]
    if continuar in "n":
        break

# Exibição do relatório em formato de tabela
print("-=" * 20)
print(f"{'RELATÓRIO DA TURMA':^40}")
print("-=" * 20)
print(f"{'Nome':<25} | {'Nota':>10}")
print("-" * 40)

soma_notas = 0
for aluno in turma:
    print(f"{aluno['nome']:<25} | {aluno['nota']:>10.1f}")
    soma_notas += aluno["nota"]

media_turma = soma_notas / len(turma)

print("-" * 40)
print(f"Média geral da turma: {media_turma:.2f}")
print("-=" * 20)