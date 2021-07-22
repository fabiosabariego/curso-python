"""
Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador perder, mostrando
o total de vitorias consecutivas que ele conquistou no final do jogo
"""

from random import randint
print('-=' * 5, end=' ')
print('JOGO PAR OU IMPAR', end=' ')
print('=-' * 5)


num = res = vit = rand = 0
sel = ''
while True:
    rand = randint(0, 11)
    print('-' * 20)
    num = int(input('Digite um Valor: '))
    sel = str(input('Par ou Impar? [P/I]')).strip().upper()
    print('-' * 20)
    res = num + rand
    if (sel == 'P' and (res % 2 == 0)) or (sel == 'I' and (res % 2 != 0)):
        print('\nParabéns, você Venceu!!!\n')
        vit += 1
    if (sel == 'P' and (res % 2 != 0)) or (sel == 'I' and (res % 2 == 0)):
        print('\nVocê Perdeu!!!\n')
        break
print('-' * 42)
print(f'O total de vitórias consecutivas foi de: {vit}')
print('-' * 42)


