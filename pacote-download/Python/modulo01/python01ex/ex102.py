"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
- O primeiro que indique o numero a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se
será mostrado ou não na tela o processo de cálculo fatorial
"""
def fatorial(n, show=False):
    from math import factorial
    if show == True:
        tot = factorial(n)
    else:
        fat = n
        tot = fat
        print('{}!'.format(n), end='= ')
        while fat > 0:
            if fat > 1:
                print('{}'.format(fat), end=' x ')
                tot = tot * (fat - 1)
            else:
                print('{}'.format(fat), end=' = ')
            fat = fat - 1
    print('{}'.format(tot))

fatorial(4)
fatorial(5, True)
fatorial(3, True)
fatorial(6)
