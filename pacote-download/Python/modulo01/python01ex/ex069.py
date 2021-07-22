"""
Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
ao usuário se ele quer continuar. No final mostre:
- Quantas pessoas tem mais de 18 anos
- Quantos homens foram cadastrados
quantas mulheres tem menos de 20 anos
"""

idade = 0
sexo = ''
cnt = 0
cont = 'S'
somidade = 0
somhomem = 0
sommulher = 0
while True:
    if cont != 'S':
        break
    else:
        idade = int(input('Idade: '))
        sexo = str(input('Sexo [F/M]: ')).strip().upper()
        cont = str(input('Deseja Confinuar? [S/N]: ')).strip().upper()
        print('-' * 30)
        if idade > 18:
            somidade += 1
        if sexo == 'M':
            somhomem += 1
        if idade < 20 and sexo == 'M':
            sommulher += 1
print(f'Temos o total de {somidade} pessoas com menos de 18 anos')
print(f'Temos {somhomem} homens cadastrados no Sistema')
print(f'Temos {sommulher} mulheres com menos de 20 anos cadastradas no sistema')
