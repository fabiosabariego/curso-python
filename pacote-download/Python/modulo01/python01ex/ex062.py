"""
Refazer o ex061, perguntando se o usuario quer mostrar mais alguns termos. O programa encerra quandoe ele colocar
0 termos.
"""
termo = int(input('Primeiro Termo: '))
raz = int(input('Razão: '))
var = 0
loop = 0
rpt = termo
novotermo = 1
termoadd = 0
while novotermo > 0:
    if var == 1:
        print('\n')
        novotermo = int(input('Quantos termos mais mostrar: '))
        termoadd += novotermo
    while loop < (10 + termoadd):
        if loop < (9 +termoadd):
            print(rpt, end=' -> ')
        else:
            print(rpt, end=' ')
        rpt += raz
        loop += 1
        var = 1
print('\nACABOU!')