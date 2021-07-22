"""  -------------------------------- CORES NO TERMINAL --------------------------------

# Para montar as cores no terminal ficara da seguinte forma

# \33[STYLE; TEXT; BACK m
# Primeiro ponto e o estilo do texto, o segundo e a cor do texto, e o terceiro a cor do fundo. O "m" e para
# fechamento da instrucao.


#a = 3
#b = 5
#print('Os valores sao \033[32m{} \033[me \033[31m{} \033[m!!!'.format(a, b))"""


nome = 'Fabio'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[0;30m'}

print('Ola, muito prazer em te conhecer {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))

