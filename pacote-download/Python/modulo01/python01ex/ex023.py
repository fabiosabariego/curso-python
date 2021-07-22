# Faça um programa para ler de 0 9999 e mostrar digitos Separados

# -------------------- TRABALHANDO COMO STRING --------------------
num = str(input('Digite um valor entre 0 e 9999: '))
num = num.replace("", " ")
print('Dezena:', num.split()[3])
print('Dezena:', num.split()[2])
print('Centena:', num.split()[1])
print('Milhar:', num.split()[0])
