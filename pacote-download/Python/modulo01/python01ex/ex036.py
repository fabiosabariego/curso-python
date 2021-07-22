# Escreva um programa para aprovar o emprestimo bancario de uma Casa. O programa deve perguntar o VALOR DA CASA, o
# SALARIO do comprador e em QUANTOS ANOS ele vai pagar. Calcular o valor da prestacao mensal, sabendo que ela nao
# pode exceder 30% do salario ou entao o emprestimo sera negado

valor = float(input('Diga o Valor do Imovel: '))
sal = float(input('Diga seu Salario: '))
prazo = int(input('Quantos anos para Pagar: '))

parcela = valor / prazo
print('O valor da casa de R${:.2f}, divido em {}x, resultara em uma parcela de R${:.2f}.'.format(valor, prazo, parcela))
if parcela > (sal * 0.30):
    print('O valor da parcela excede a 30% do valor do comprador (R${:.2f}), emprestimo negado!'.format(sal * 0.30))
elif parcela <= (sal * 0.30):
    print('O valor e inferior a 30% do salario (R#{:.2f}), emprestimo liberado!'.format(sal * 0.30))
