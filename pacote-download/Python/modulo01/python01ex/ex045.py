"""
Crie um programa que faça o computador jogar jokenpo com você
"""
import random
import time
itens = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(0, 2)
print('========== VAMOS JOGAR UM JOKENPÔ? ==========')
esc = int(input("""=============================================
(0) - Pedra
(1) - Papel
(2) - Tesoura
Escolha qual sua Jogada: """))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')

print('-=' * 14)
print('Você Jogou {}'.format(itens[esc]))
print('Computador Jogou {}'.format(itens[pc]))
print('-=' * 14)

if (pc == 0 and esc == 0) or (pc == 1 and esc == 1) or (pc == 2 and esc == 2):
    print('Empate!!!')
elif (pc == 0 and esc == 1) or (pc == 1 and esc == 2) or (pc == 2 and esc == 0):
    print('Você Venceu!!!')
elif (pc == 0 and esc == 2) or (pc == 1 and esc == 0) or (pc == 2 and esc == 1):
    print('Você Perdeu!!!')