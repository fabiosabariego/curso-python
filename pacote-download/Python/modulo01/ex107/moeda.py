"""
Trabalhando com Modularização -- Esse projeto será um espécie de Biblioteca
"""

def aumentar(moeda, aum=0):
    res = (moeda * (aum/100))+moeda
    return res


def diminuir(moeda, dim=0):
    res = moeda-(moeda * (dim/100))
    return res


def dobro(moeda):
    res = moeda * 2
    return res


def metade(moeda):
    res = moeda / 2
    return res