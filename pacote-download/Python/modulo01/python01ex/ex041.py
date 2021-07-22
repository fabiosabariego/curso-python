'''
Confederacao Nacional de Natacao ler o ano de nascimento do atleta e mostrar qual categoria esta
- ate 9 anos = Mirim
- Maior que 9 e ate 14 = Infantil
- Maior que 14 e ate 19 = Junior
- Maior que 19 e ate 20 = Senior
- Maior que 20 = Master
'''

from datetime import date
ano = int(input('Qual ano de Nascimento: '))
hoje = date.today()
atual = hoje.year

nasceu = atual - ano

if nasceu <= 9:
    print('Voce tem {} anos, entao sua categoria e a Mirim'.format(nasceu))
elif nasceu > 9 and nasceu <= 14:
    print('Voce tem {} anos, entao sua categoria e a Infantil'.format(nasceu))
elif nasceu > 14 and nasceu <= 19:
    print('Voce tem {} anos, entao sua categoria e a Junior'.format(nasceu))
elif nasceu > 19 and nasceu <= 20:
    print('Voce tem {} anos, entao sua categoria e a Senior'.format(nasceu))
elif nasceu > 20:
    print('Voce tem {} anos, entao sua categoria e a Master'.format(nasceu))
