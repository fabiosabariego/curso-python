"""
Criar programa para ler o ano de nascimento de 7 pessoas. Mostrar quandas não atingiram a maioridade e quantas atingiram
"""
from datetime import date

ano = 0
idade = 0
menor = 0
maior = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da pessoa {}: '.format(c)))
    idade = date.today().year - ano
    if idade < 21:
        menor = menor + 1
    else:
        maior = maior + 1
print('Conforme as 6 idades digitadas, {} são maiores de 21, e {} são menores de 21 anos!'.format(maior, menor))