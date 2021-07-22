'''
Leia 2 notas e calcule a media de um aluno
- Abaixo de 5 sera Reprovado
- entre 5 e 6.9 em recuperacao
- Acima de 7 aprovado
'''

n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1 + n2)/2

if media < 5:
    print('Aluno(a) reprovado(a) com nota {:.2f}'.format(media))
elif media >= 5 and media <=6.9:
    print('Aluno(a) em Recuperacao com nota {:.2f}'.format(media))
else:
    print('Aluno(a) Aprovado(a) com media superior a {:.2f}'.format(media))
