""" TRABALHANDO COM CONDIÇÕES ANINHADAS - IF / ELIF / ELSE """

nome = str(input("Digite seu Nome: "))
if nome == "Fabio":
    print("Que nome Bonito, {}".format(nome))
elif nome == "Gustavo":
    print("Esse é o nome do seu professor, {}".format(nome))
else:
    print("Não reconheço esse nome {}".format(nome))