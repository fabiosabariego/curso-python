"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho. Cadastre-os (com idade) em um dicionario
se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o Salario.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
"""

from datetime import date
ano = date.today().year
dados = dict()

dados['Nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de Nascimento: '))
dados['Idade'] = ano - nasc
dados['CTPS'] = int(input('Carteira de Trabalho (0 Não Tem): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = (dados['Contratação'] - nasc) + 35
print('-=' * 60)

for k, v in dados.items():
    print(f'{k} tem o valor de {v}')

