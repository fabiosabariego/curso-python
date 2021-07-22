"""
Desenvolver programa que leia 4 numeros pelo teclado e guarde-os em uma tupla. No final mostre
- Quantas vezes o 9 apareceu
- em que posição foi digitado o primeiro valor 3
- quais foram os numeros pares
"""

num = (int(input('Digite um valor: ')),
        int(input('Digite outro Valor: ')),
        int(input('Digite mais um Valor: ')),
        int(input('Digite o ultimo Valor: ')))
print('=' * 50)
print(f'Os numerdos digitados foram {num}')
print('=' * 50)
print(f'O numero 9 apareceu: {num.count(9)}')
if 3 in num:
    print(f'O numero 3 apareceu primeiro na posição: {num.index(3) + 1}')
else:
    print('Não foram digitados números 3!')
print('Os numeros pares Digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n}', end=' ')
