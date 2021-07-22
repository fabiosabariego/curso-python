# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cid = str(input('Diga o nome da sua Cidade: '))
nome = cid.split()[0].upper()
print('Seu nome começa com Santo:', 'SANTO' in nome)
