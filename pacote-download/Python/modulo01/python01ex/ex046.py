"""
Fazer um contador regressivo para estouro de fogos, de 10 a 0 segundos, com uma pausa de 1s entre eles
"""

from time import sleep
print('=' * 35)
print('Contagem Regressiva - Final de Ano')
print('=' * 35)

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('Feliz Ano Novo!!!!')