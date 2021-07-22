"""
Refaça o desafio 9, mostrando a tabuada do numero que o usuário escolher, só que faça com for
"""
res = 0
num = int(input('Digite um numero: '))
print('=' * 20)
print('A Tabuada do {} é:'.format(num))
print('=' * 20)
for c in range(1, 11):
    res = num * c
    print('{} x {} = {}'.format(num, c, res))
