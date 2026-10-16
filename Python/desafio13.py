jogador = {}
total_gols = []

jogador['nome'] = str(input("Digite o nome do jogador: "))
jogador['partidas'] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for partida in range(jogador['partidas']):
    gols = int(input(f"Quantos gols o {jogador['nome']} fez na {partida + 1}° partida? "))
    total_gols.append(gols)

jogador['gols'] = total_gols
jogador['total'] = sum(total_gols)

print("-=" * 30)
print(jogador)
print("-=" * 30)

# Exibição detalhada de cada partida
print(f"O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.")
for i, g in enumerate(jogador["gols"]):
    print(f"   => Na partida {i + 1}, fez {g} gols.")

print(f"Foi um total de {jogador['total']} gols.")
print("-=" * 30)