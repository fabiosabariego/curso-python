"""
Crie um Programa onde o usuario possa digitar 5 valores numericos e cadastre-os em uma lista, já na posição correta
de inserção (Sem usar o Sort)
No final mostre a lista ordenada na tela
"""

num = []
for c in range(0, 5):
    valor = int(input('Digite um Valor: '))
    if c == 0 or valor > num[-1]:
        num.append(valor)
        print('Adicionado ao Final da Lista')
    else:
        pos = 0
        while pos < len(num):
            if valor <= num[pos]:
                num.insert(pos, valor)
                print(f'Adicionado na Posição {pos} da lista')
                break
            pos += 1
print(f'Os valores adicionados foram: {num}')

