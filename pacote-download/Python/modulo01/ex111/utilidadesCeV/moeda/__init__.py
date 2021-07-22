"""
Trabalhando com Modularização -- Esse projeto será uma espécie de Biblioteca
"""


def aumentar(valor=0, aum=0, f=False):
    res = (valor * (aum / 100)) + valor
    if f == True:
        return moeda(res)
    else:
        return res


def diminuir(valor=0, dim=0, f=False):
    res = valor-(valor * (dim/100))
    if f == True:
        return moeda(res)
    else:
        return res


def dobro(valor=0, f=False):
    res = valor * 2
    if f == True:
        return moeda(res)
    else:
        return res


def metade(valor=0, f=False):
    res = valor / 2
    if f == True:
        return moeda(res)
    else:
        return res


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:<8.2f}'.replace('.', ',')

"""
Na configuração >8.2f Temos:
>   significa alinhado a direita
8   signiifica com 8 elementos no total
.2f significa com duas casas decimais

Sendo assim, ele ficará como 000000.00, alinhado a direita
"""


def resumo(valor=0, aumenta=10, diminui=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(valor)}')
    print(f'Dobro do Preço: \t{dobro(valor, True)}')
    print(f'Metade do Preço: \t{metade(valor, True)}')
    print(f'{aumenta}% de Aumento: \t{aumentar(valor, aumenta, True)}')
    print(f'{diminui}% de Aumento: \t{diminuir(valor, diminui, True)}')
