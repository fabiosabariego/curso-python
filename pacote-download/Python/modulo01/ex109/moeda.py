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
    return f'{moeda}{valor:.2f}'.replace('.', ',')

"""
Na configuração >8.2f Temos:
>   significa alinhado a direita
8   signiifica com 8 elementos no total
.2f significa com duas casas decimais

Sendo assim, ele ficará como 000000.00, alinhado a direita
"""