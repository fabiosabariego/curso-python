# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente

nome = str(input('Diga seu nome: ')).strip()
lista = nome.split()
indice = len(lista) - 1
print('Primeiro Nome: {}'.format(nome.split()[0]))
print('Ultimo Nome: {}'.format(lista[indice]))
