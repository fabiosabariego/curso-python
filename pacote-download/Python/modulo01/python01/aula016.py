"""
FUNCIONAMENTO DE TUPLAS

TUPLA USAMOS ()
LISTA USAMOS []
DICIONÁRIO USAMOS {}
"""
"""
lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata')
print(lanche[1])
print(lanche[1:3])
print(lanche[:2])
print(lanche[-2:])

for c in lanche:
    print(f'Eu vou comer {c}')
print('=' * 50)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('=' * 50)

for pos, cnt in enumerate(lanche):
    print(f'Eu vou comer {cnt} na posição {pos}')
print('=' * 50)

print(sorted(lanche))
"""

"""
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(c)
print(d)
print(c.count(5))       # Mostra quandos elementos 5 existem dentro da Tupla c.
print(c.index(8))       # Mostra em que posição está o numero 8 dentro da Tupla c.
print(c.index(5, 1))    # Mostra a posição do numero 5, a partir da posição 1 (a posição 0 é ignorada neste caso)
"""

pessoa = ('Gustavo', 39, 'Masculino', 99.88)
del(pessoa)             # O comando del apaga qualquer coisa da memória, nesse caso não irá imprimir pois "pessoa" será deletado
print(pessoa)