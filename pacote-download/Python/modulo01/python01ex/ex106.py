"""
Faça um mini-sistema que utilize o interactive help do Python. O usuário vai digitar o comando e o manual vai
aparecer. Quando o usuário digitar FIM, o programa irá encerrar.
OBS: Use Cores
"""
from time import sleep

c = ('\033[m',          # 0 - sem cor
    '\033[0;30;41m',    # 1 - Vermelho
    '\033[0;30;42m',    # 2 - Verde
    '\033[0;30;43m',    # 3 - Amarelo
    '\033[0;30;44m',    # 4 - Azul
    '\033[0;30;45m',    # 5 - roxo
    '\033[7;97m'        # 6 - Branco
    );

def escreva(msg, cor=0):
    print(c[cor], end='')
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))
    print(c[0], end='')


def ajuda(fun, cor=0):
    print(c[cor], end='')
    print(help(fun))
    print(c[0], end='')


while True:
    escreva('Sistema de Ajuda PyHELP', 2)
    escolha = str(input('Função ou Biblioteca: ')).strip().lower()
    if escolha.upper() == 'FIM':
        break
    else:
        escreva(f"Acessando o manual do comando '{escolha}'", 4)
        sleep(1.5)
        ajuda(escolha, 6)
        sleep(1.5)

escreva('ATÉ LOGO!!!', 3)
