"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
O nome de um jogador e quantos gols ele marcou
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente
"""

def ficha(jog='Desconhecido', gols='0'):
    return f'O Jogador {jog} fez {gols} gol(s)'

jog = str(input('Nome do jogador: ')).strip()
gol = str(input('Gols do Jogador: '))

if len(gol) != 0 and len(jog) != 0:
    print(ficha(jog, int(gol)))
elif len(gol) == 0 and len(jog) != 0:
    print(ficha(jog=jog))
elif len(gol) != 0 and len(jog) == 0:
    print(ficha(gols=gol))
else:
    print(ficha())
