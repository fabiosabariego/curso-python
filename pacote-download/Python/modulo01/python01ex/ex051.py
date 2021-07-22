"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão
"""
pt = int(input('Primeiro Termo: '))
raz = int(input('Razão: '))
dec = pt + (10-1) * raz
for c in range(pt, dec + raz, raz):
    print(c, end=' -> ')
print('ACABOU!')