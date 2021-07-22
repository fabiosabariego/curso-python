"""
Crie um programa que leia varios números inteiros pelo teclado. O programa só vai parar quando o usuario digitar 999
No final mostre quantos numeros foram digitados e qual foi a soma entre eles (Desconsiderar o 999)

É o mesmo que o ex 64, porém agora vamos usar a condição break da função while
"""

num = cnt = som = 0
while True:
    num = int(input('Digite um valor [999 parar]: '))
    if num == 999:
        break
    cnt += 1
    som += num
print(f'Foram digitados {cnt} numeros, e a soma deles é {som}')