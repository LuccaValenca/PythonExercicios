#Leia um nome e diga se possui "SILVA no nome"

nome = str(input("Informe o nome completo: ")).strip()

print("{} {} \"SILVA\"".format(nome, str("SILVA" in nome.upper())).replace("True", "contém").replace("False", "não contém"))
