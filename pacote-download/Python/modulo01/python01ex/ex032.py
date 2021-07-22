# Fazer um programa que leia um ano qualquer e mostre se ele e bissexto

from datetime import date
ano = int(input('Digite os quatro digitos de um ano: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 ==0 and ano != 100) or (ano % 400 == 0):
    print('O ano {}  e Bissexto'.format(ano))
else:
    print('O ano {} nao e Bissexto'.format(ano))
