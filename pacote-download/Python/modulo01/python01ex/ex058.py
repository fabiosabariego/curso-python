"""
Melhore o Jogo do Desafio 28 onde o computador vai "pensar" em um numero entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
"""

from random import randrange
rand = randrange(0, 10)
n1 = 20
while rand != n1:
    n1 = int(input('Digite um valor de 0 a 10: '))
    if n1 != rand:
        print('Você Errou, o número aleatório é {}, tente novamente!'.format(rand))
print('Parabéns, você acertou o número!!!')