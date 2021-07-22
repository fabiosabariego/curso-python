"""
Crie uma tupla preenchida com os 12 primeiros colocados da tabela do brasileirão, na ordem de colocação.
depois mostre:
- Apenas os 5 primeiros colocados
- Os ultimos 4 colocados
- Uma Lista com os times em ordem alfabética
- Em que Posição está o chapecó
"""
times = ('Santos', 'Palmeiras', 'São Paulo', 'Corinthians', 'Flamengo', 'Vasco', 'Cruzeiro', 'Atletico GO', 'Atlético MG', 'Chapecoense', 'Bahia', 'Botafogo')
print('-=' * 30)
print(f'Times Brasileirão: {times}')
print('-=' * 30)
print(f'Os cinco primeiro são: {times[:5]}')
print('-=' * 30)
print(f'Os 4 Ultimos são: {times[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 30)
print(f"A chapecoense está na {times.index('Chapecoense') + 1} posição.")
print('-=' * 30)