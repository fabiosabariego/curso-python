"""
Fazer Programa que calcule a soma entre todos os numeros impares que são multiplos de 3 e estão no intervalo
entre 1 e 500
"""
res = 0
for c in range(1, 501):
    if c % 3 == 0:
        res = res + c
print('A soma dos Numeros multiplos de 3, no intervalo entre 1 e 500 é: {}'.format(res))
