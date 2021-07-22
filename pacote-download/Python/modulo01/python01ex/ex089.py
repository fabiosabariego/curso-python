"""
Crie um programa que leia o nome e duas notas de varios alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada
aluno individualmente
"""
from time import sleep
boletim = list()
tot = 0
while True:
        nome = str(input('Nome: ')).strip()
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        media = (nota1 + nota2) / 2
        resp = str(input('Continuar: [S/N]: ')).strip().upper()
        boletim.append([nome, [nota1, nota2], media])
        if resp in 'N':
            break
print('-=' * 15)
print(f'{"No.":<6}{"NOME":<10}{"MÉDIA":>6}')
print('-' * 25)
while tot < len(boletim):
    print(f'{tot:<6}{boletim[tot][0]:<10}{boletim[tot][2]:>6.2f}')
    tot += 1
print('-' * 45)
while True:
    notaluno = int(input('Mostrar Notas de Qual Aluno? (999 Interrompe): '))
    if notaluno == 999:
        break
    else:
        print('-' * 45)
        print(f'Notas de {boletim[notaluno][0]} são {boletim[notaluno][1]}')
    print('-' * 45)
sleep(1)
print('FINALIZANDO...')
sleep(1)
print('<<< VOLTE SEMPRE >>>')