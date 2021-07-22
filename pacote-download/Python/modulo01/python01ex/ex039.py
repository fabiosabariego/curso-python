'''
Fazer um programa para ler o ano de nascimento de um jovem e informar de acordo com a idade:
- Se ele ainda vai se alistar ao exercito
- Se e a hora de se alistar
- Se ja passou do tempo de se alistar

E ainda mostrar o tempo que falta e o prazo que passou
'''

from datetime import date
ano = int(input('Diga o ano em que nasceu: '))
hoje = date.today().year
idade = hoje - ano


if idade < 18:
    alistar = 18 - idade
    print('Voce tem {} anos, ainda faltam {} anos para o alistamento!'.format(idade, alistar))
elif idade == 18:
    print('Voce tem {} anos, esta na epoca de se alistar!'.format(idade))
else:
    passou = idade - 18
    print('Voce tem {} anos, passou {} anos do alistamento!'.format(idade, passou))
