"""
Faça um programa que tenha um função chamada area(), que recebe as dimensões de um terreno retangular(largura e comp)
e mostre a area do terreno
"""

def area(l, c):
    res = l * c
    print(f'A área de um terreno de {l:.1f} x {c:.1f} é de {res:.1f}m²')


print('Controle de Terrenos')
print('-' * 30)
larg = float(input('LARGURA(m): '))
comp = float(input('COMPRIMENTO(m): '))
area(larg, comp)
