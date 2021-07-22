# ------------------------------ OPERADORES MATEMATICOS ------------------------------
# ** -> Potencia
# // -> Divisão Inteira
# %  -> Resto da Divisão

# ------------------------------- ORDEM DE PROCEDENCIA -------------------------------
# Primeiro: Parenteses () -> Será realizada qualquer operação matemática dentro dos parênteses Primeiro
# Segundo:  Potencia   ** -> Em seguida será realizada qualquer operação de potência
# Terceiro: Operadores Matemáticos -> *, /, // e %
# Quarto:   Operadores de Soma e Subtração -> + e -
# ------------------------------------------------------------------------------------

# ---- nome = input('Qual seu nome? ')
# ---- print('Prazer em te conhecer {:<20}!'.format(nome))

# - Dentro das Chaves {} acima, os valores representam o seguinte:
# {:20} -> Significa que o campo nome terá 20 caracteres (Se forem usados 5 ele preencherá o restante com espaços)
# {:<20} -> Significa que o campo nome terá 20 caracteres com alinhamento das letras à Esquerda
# {:>20} -> Significa que o campo nome terá 20 caracteres com alinhamento das letras à Direita
# {:^20} -> Significa que o campo nome terá 20 caracteres com alinhamento das letras Centralizado
# {:=^20} -> Significa que o campo nome terá 20 caracteres, o nome ficará da seguinte forma: =====nome=====

n1 = int(input('Um Valor: '))
n2 = int(input('Outro Valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o Produto é {} \n a divisão é {:.2f}.'.format(s,m,d),  end='')
print('A Divisão intera é {} e a Potência é {}'.format(di,e))