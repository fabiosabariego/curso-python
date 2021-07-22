"""
Crie um Programa onde o usuario digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
se a expressão passada está com os parênteses abertos ou fechados na ordem correta
"""

exp = str(input('Digite sua Expressão: '))
lista = []
for simb in exp:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) != 0:
    print('Sua expressão está errada...')
else:print('Sua expressão está correta, parabéns!!!!')