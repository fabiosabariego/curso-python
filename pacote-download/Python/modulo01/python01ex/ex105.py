"""
Faça um programa que tenha uma função chamada notas() que pode receber várias notas de alunos e vai retornar um
dicionário com as seguintes informações:
- Quantidade de Notas
- Maior Nota
- Menor Nota
- Média da Turma
- Situação (opcional)

adicione também as docstring da função
"""

def notas(*n, sit=False):
    """
    -> Função para Analisar notas e situações de vários alunos
    Param. n: Uma ou mais notas dos alunos (aceita varias)
    Param. sit: Valor Opcional, indicando se deve ou não adicionar a situação
    return: Dicionário com várias informações sobre a situação da turma
    """
    res = {}
    soma = 0
    for v in n:
        soma += v
    med = soma / len(n)
    res['Total'] = len(n)
    res['Maior'] = max(n)
    res['Menor'] = min(n)
    res['Media'] = f'{med:.1f}'
    if sit == True:
        if med < 5:
            res['Situação'] = 'RUIM'
        elif 5 < med < 7:
            res['Situação'] = 'RAZOÁVEL'
        else:
            res['Situação'] = 'BOA'
    return res

resp = notas(8.2, 2.6, 5.7, 8.3, 9.92, sit=True)
print(resp)