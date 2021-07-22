"""
Crie um Programa que tenha uma tupla com varias palavras (não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais
"""
tupla = ('Estudar', 'Aulas', 'Python', 'Cereja', 'Carro', 'Viajar', 'Trabalho', 'Uva', 'Batatinha')

for c in tupla:
    print(f'\nNa palavra {c} temos as vogais: ', end='')
    for vogal in c:
        if vogal in 'aAeEiIoOuU':
            print(vogal, end=' ')
