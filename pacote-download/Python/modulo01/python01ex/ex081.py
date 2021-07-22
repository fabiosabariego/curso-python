"""
Crie um Programa para ler Varios Numeros e colocar em lista, depois mostre:

- Quantos Numeros foram digitados
- A lista de valores ordenadas de forma decrescente
- Se o valor 5 foi digitado e está ou não na lista
"""

num = []
cont = ''
while True:
    if cont != 'N':
        num.append(int(input('Digite um Valor: ')))
        cont = str(input('Deseja Continuar? [S/N]: ')).strip().upper()
    else:
        break
num.sort(reverse = True)
print(f'Foram Digitados {len(num)} valores!')
print(f'Os valores digitados em forma decrescente ficam: {num}')
if 5 in num:
    print('O Valor 5 foi digitado!')
else:
    print('O Valor 5 não foi digitado!')