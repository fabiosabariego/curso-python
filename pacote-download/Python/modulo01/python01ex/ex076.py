"""
Crie um programa que tenha uma tupla unica com nomes de produtos e seus preços na sequência
No final, mostre uma listagem de preços , organizando os dados de forma tabular
"""

print('-' * 50)
print('LISTAGEM DE PREÇOS'.center(50))
print('-' * 50)
tupla = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for c in range(0, len(tupla), 2):
    print(f'{tupla[c]:.<41}R${tupla[c+1]:>7.2f}')
print('-' * 50)