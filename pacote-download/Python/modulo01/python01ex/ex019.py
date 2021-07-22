# Professor quer sortear 4 alunos para apagar o quadro. Faça um programa para ler o nome dos alunos, e escrever qual nome foi escolhido

import random
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))

alunos = [a1, a2, a3, a4]

sort = random.choice(alunos)

print('O aluno sorteado para limpar a lousa é: {}'.format(sort))
