# Crie um Programa que leia o nome completo de uma pessoa e mostre:
# Nome todas as letras maiúsculas
# Minusculas
# Quantas letras (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Digite Nome Completo: '))

print('Nome Completo Maiúscula:', nome.upper())
print('Nome Completo Minuscula:', nome.lower())
print('Total de Letras sem Espaços:', len(nome.replace(" ", "")))
print('Quantidade Letras Primeiro Nome:', len(nome.split()[0]))
