"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 a 20.
Seu programa deverá ler um numero pelo teclado (0..20) e mostra-la por extenso
"""

tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
num = int(input('Digite um Numero: '))
while num < 0 or num > 20:
    num = int(input('Numero Inválido, Digite Novamente: '))
print(f'O numero que você digitou é {tupla[num]}')

