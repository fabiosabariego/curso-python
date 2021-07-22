# Escrever um programa que faça o computador pensar em um numero inteiro entre 0 e 5
# Fazer um campo para o usuario tentar acertar esse numero e mostrar a mensagem se venceu ou perdeu

import random
from time import sleep
n1 = int(input('Digite um valor de 0 a 5: '))
rand = random.randrange(0, 5)
print('Processando...')
sleep(3)
if n1 == rand:
    print('Você Acertou, Parabéns!!')
else:
    print('Infelizmente você errou!')
