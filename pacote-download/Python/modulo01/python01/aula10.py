#  ----------------------------- CONDITIONS -----------------------------

# nome = str(input('Qual Seu nome? '))
# if nome == 'Fabio':
#    print('Que nome lindo você tem!!')
#    print('Seja muito bem vindo {}'.format(nome))
# else:
#    print('o nome {} não foi encontrado no nosso banco de dados!!'.format(nome))


# nome = str(input('Qual Seu nome? '))
# if nome == 'Fabio':
#    print('Que nome lindo você tem!!')
# print('Seja muito bem vindo {}'.format(nome)) # Tomar Cuidado com Identação, neste caso essa mensagem sempre irá aparecer


n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
m = (n1 + n2) / 2
if m >= 6.0:
    print('Sua média foi {:.1f}, e ela foi muito boa, Parabéns!'.format(m))
else:
    print('Sua média foi {:.1f}, e ela não foi muito boa, estude mais!'.format(m))
