"""
Faça um programa que tenha uma função chamada contador e receba 3 parâmetros: inicio, fim e passo e realize a contagem.
Seu programa tem que realizar 3 contagens através da função criada:
- De 1 até 10 de 1 em 1
- de 10 até 0 de 2 em 1
- Uma contagem personalizada
"""

def contagem(i, f, p):
    from time import sleep
    print('-=' * 20)
    if p < 0:
        p *= -1
    elif p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if f > i:
        for c in range(i, f + p, p):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
    elif f < i:
        for v in range(i, f - p, -p):
            print(v, end=' ')
            sleep(0.5)
        print('FIM!')

contagem(1, 10, 1)
contagem(10, 0, 2)

print('-=' * 20)
print('Agora é a sua vêz de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)