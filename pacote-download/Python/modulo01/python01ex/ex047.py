"""
Crie um programa que mostre na tela todos os numeros pares que estão no intervalo de 1 a 50.
"""
print('Numeros Pares que estão entre 1 e 50:')

for c in range(1, 51, 1):
    if c % 2 == 0:
        print(c)
