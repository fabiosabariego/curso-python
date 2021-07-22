"""
Pacote para validação de dados de entrada:
- Não pode ser letra
- Não pode ser espaço vazio
- Deve ter apenas numeros
"""


def leiaDinheiro(msg=''):
    valido = False
    while not valido:
        val = str(input(msg)).strip().replace(',', '.')
        if val.isalpha() or val == '':
            print(f'\033[1;31mERRO: \"{val}\" é um preço inválido!!', end='')
            print('\033[0;0m')
        else:
            valido = True
            return float(val)
