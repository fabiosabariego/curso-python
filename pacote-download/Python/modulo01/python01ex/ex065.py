"""
Crie um programa que leia varios numeros inteiros pelo teclado. No final mostre a media entre todos os valores e
qual foi o maior e o menor valor lido. O programa deve perguntar ao usuario se ele quer ou nao continuar digitando
valores
"""

num = 0
conf = ''
med = 0
cnt = 0
maior = 0
menor = 0
while conf != 'n':
    num = int(input('Digite um valor: '))
    cnt += 1
    med = (med + num) / cnt
    print('=================')
    conf = str(input('Continuar? [Y/N]: ')).lower()
    print('\n')
    if cnt == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('A media é: {:.1f}'.format(med))
print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))
