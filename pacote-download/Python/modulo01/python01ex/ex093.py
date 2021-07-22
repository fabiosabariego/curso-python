"""
Crie um Programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em
um Dicionário, incluindo o total de gols feitos durante o campeonato
"""

jogador = {}
gols = []
total = 0

jogador['Nome'] = str(input('Nome do Jogador: ')).strip()
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))
    total += gols[c]
jogador['Gols'] = gols
jogador['Total'] = total

print('-=' * 35)
print(jogador)
print('-=' * 35)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 35)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')

for c in range(0, partidas):
    print(f'    => Na partida {c}, fez {jogador["Gols"][c]} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
