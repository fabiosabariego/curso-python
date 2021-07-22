"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final mostre:
- A média de Idade do Grupo
- Qual nome do homem mais velho
- Quantas mulheres tem menos de 20 anos
"""
medidade = 0
velho = 0
mulher = 0
man = ""
for c in range(1, 5):
    print('-------- PESSOA {} --------'.format(c))
    nome = str(input('Nome: '.format(c))).strip()
    idade = int(input('Idade: '.format(c)))
    sexo = str(input('Sexo [M/F]: '.format(c))).upper().strip()
    medidade += idade
    if idade > velho and sexo == 'M':
        velho = idade
        man = nome
    if idade < 20 and sexo == 'F':
        mulher = mulher + 1

print('\n')
print('=' * 50)
if velho != 0:
    print('A média de idade do grupo é de {:.1f} anos!'.format(medidade / c))
    print('-' * 50)
    print('O nome do Homem mais velhor é: {}'.format(man))
else:
    print('-' * 50)
    print('Não existem homens nesse grupo!')
if mulher != 0:
    print('-' * 50)
    print('Nesse Grupo existem {} mulher(es) com menos de 20 anos!'.format(mulher))
else:
    print('-' * 50)
    print('Não existem mulheres com menos de 20 anos nesse grupo!')
print('=' * 50)
