"""
Faça um programa que mostra a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario.
O programa será interrompido quando o numero solicitado for negativo
"""

num = cnt = tab = 0
while True:
    print('-' * 50)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 50)
    if num < 0:
        break
    tab = 0
    cnt = 0
    while cnt < 10:
        cnt += 1
        tab = num * cnt
        print(f'{num} x {cnt} = {tab}')
print('Programa encerrado!! Volte Sempre!!')