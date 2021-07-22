"""
Escreva um programa que leia um número n inteiro e mostre a tela os n primeiros elementos de uma sequencia de fibonacci

F(n + 2) = F(n + 1) + F(n) , com n ≥ 1 e F(1) = F(2) = 1

"""

n = int(input('Digite um Numero: '))
t1 = 0
t2 = 1
inc = 3
print('{} -> {}'.format(t1, t2), end=' -> ')
while inc <= n:
    inc += 1
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print('{}'.format(t3), end=' -> ')
print('FIM!!!')