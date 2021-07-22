"""
Crie um Programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário, e
todos os dicionários em uma lista. No final, mostre:
- Quantas pessoas foram cadastradas
- A média de Idade do grupo
- Uma lista com todas as mulheres
- Uma lista com todas as pessoas com idade acima da média
"""
pessoas = {}
lista = []
soma = media = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: ')).strip()
    while True:
        pessoas['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if pessoas['Sexo'] in 'MF':
            break
        print('ERRO!! Digite apenas M ou F!!')
    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']

    lista.append(pessoas.copy())
    while True:
        conf = str(input('Continuar? [S/N]: ')).strip().upper()
        if conf in 'SN':
            break
        print('ERRO!! Digite apeas S ou N!!')
    if conf == 'N':
        break

media = soma / len(lista)
print('-=' * 40)
print(f'- O grupo tem {len(lista)} pessoas')
print(f'- A média de idade do grupo é {media:5.2f} anos')

print('- As mulheres cadastradas foram:', end=' ')
for m in lista:
    if m['Sexo'] == 'F':
        print(f'{m["Nome"]}', end=' ')
print()
print('-' * 60)
print('- A lista das pessoas com idade acima da média: ')
print()
for p in lista:
    if p['Idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v}', end='; ')
        print()