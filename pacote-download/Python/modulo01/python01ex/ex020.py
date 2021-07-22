# Sorteio de 4 alunos para apresentação de trabalhos, mostrar o nome dos 4 alunos e a ordem sorteada

import random

a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))

alunos = [a1, a2, a3, a4]

sort = random.sample(alunos, k=4) # Podemos também utilizar a função random.shuffle

print('A ordem de apresentação será: {}'.format(sort))
