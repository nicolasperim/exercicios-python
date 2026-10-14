def verificar_aprovacao(aluno):
    """Verifica se o aluno foi aprovado ou reprovado pela nota."""
    if aluno["nota"] >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"


# Programa Principal
boletim = {}

boletim["nome"] = input("Qual o nome do aluno? ")

while True:
    boletim["nota"] = float(input("Qual a nota final do aluno? "))
    if boletim["nota"] < 0 or boletim["nota"] > 10:
        print("A nota final só pode ser de 0 a 10. Tente novamente.")
    else:
        break

situacao = verificar_aprovacao(boletim)

print(f"O aluno {boletim['nome']} está {situacao} com nota {boletim['nota']}.")