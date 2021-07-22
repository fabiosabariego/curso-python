"""
Aprimore o ex093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador.
"""

jogador = {}
gols = []
time = []
while True:
    total = 0
    jogador['Nome'] = str(input('Nome do Jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c}: ')))
        total += gols[c]
    jogador['Gols'] = gols[:]
    jogador['Total'] = total
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    while True:
        resp = str(input('Continuar? [S/N]: ')).strip().upper()
        if resp in 'SN':
            break
        print('Erro!! O valor digitado não existe!!!')
    if resp == 'N':
        break
print('-=' * 50)
print(f'{"No.":<6}{"NOME":<16}{"GOLS":<16}{"Total":<16}')
print('-' * 50)

for k, v in enumerate(time):
    print(f'{k:<6}', end='')
    for d in v.values():
        print(f'{str(d):<16}', end='')
    print()

while True:
    print('-' * 50)
    jog = int(input('Mostrar dados de qual Jogador? [999 para sair]: '))
    if jog != 999:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[jog]["Nome"]}')
        for c in range(len(time[jog]["Gols"])):
            print(f'No Jogo {c}, fez {time[jog]["Gols"][c]} gols.')
    else:
        break