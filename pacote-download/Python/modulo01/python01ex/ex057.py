"""
Faça o programa que leia o sexo de uma pessoa, mas só aceite os valores F e M. Caso esteja errado, peça a digitação
Novamente.
"""
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Sexo [F/M]: ')).upper()
    if sexo not in "FM":
        print('Valor não Conhecido, digite apenas F ou M.')
if sexo == 'M':
    print('O Sexo escolhido foi Masculino!')
elif sexo == 'F':
    print('O Sexo escolhido foi o Feminino!')
