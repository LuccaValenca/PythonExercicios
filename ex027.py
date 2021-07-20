# Leia o nome completo e mostre o nome e sobrenome

nome = str(input("Informe o nome completo: ")).strip()

print("Primeiro nome: {}\nSobrenome: {}".format(nome.split()[0], nome.split()[len(nome.split())-1]))
