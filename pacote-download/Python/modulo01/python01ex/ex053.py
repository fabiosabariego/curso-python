"""
Crie um Programa que leia uma Frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
"""

frase = str(input('Digite uma frase: ')).replace(" ", "").upper()
if frase == frase[::-1]:
    print('A Frase Digitada ao contrário é idêntica à ela escrita normal, ela é Palíndromo!')
else:
    print('A Frase Digitada ao contrário não é idêntica à ela escrita normal, ela não é Palíndromo!')
