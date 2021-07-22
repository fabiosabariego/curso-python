"""
Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999.
No final mostre quantos numeros foram digitados e qual foi a soma entre eles, desconsiderando o flag (999)
"""

num = res = count = 0
while num != 999:
    num = int(input('Digite um valor [999] para parar: '))
    if num != 999:
        res += num
        count += 1
print('Foram digitados {} numeros, e a soma entre eles é: {}'.format(count, res))
