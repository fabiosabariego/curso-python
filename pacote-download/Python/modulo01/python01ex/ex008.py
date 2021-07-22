# ------------------------- DESAFIO 008 -------------------------
# Ler um valor em metros, converter e exibir para centimetros e milímetros

m = float(input('Digite um valor: '))

cm = m * 100
mm = m * 1000

print('O valor digitado foi de {:.4f}m, isso equivale a {:.2f}cm e também {:.2f}mm'.format(m, cm, mm))