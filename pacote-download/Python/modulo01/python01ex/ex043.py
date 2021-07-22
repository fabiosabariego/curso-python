"""
Desenvolva uma Lógica que leia o peso e altura de uma pessoa, calcule o IMC e mostre seu status, de acordo
com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- Acima de 40: Obesidade Mórbida
"""

altura = float(input('Digite sua Altura: '))
peso = float(input('Digite seu Peso: '))

imc = peso/(altura ** 2)
if imc < 18.5:
    print('Seu IMC é {:.1f}, você está abaixo do peso!'.format(imc))
elif 18.5 < imc <= 25:
    print('Seu IMC é {:.1f}, você está no Peso Ideal!'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é {:.1f}, você está com Sobrepeso!'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é {:.1f}, você está com Obesidade!'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.1f}, você está com Obesidade Mórbida!'.format(imc))