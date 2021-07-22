# Crie um Programa que leia o nome de uma pessoa e diga se ela tem silva no nome

nome = str(input('Diga seu Nome: '))
min = nome.lower()
print('Tem Silva no nome: ', 'silva' in min)
