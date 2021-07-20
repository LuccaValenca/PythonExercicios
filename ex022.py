'''
Leia o nome completo e:

1 - Exibir nome em maiusculas
2 - Exibir nome em minusculas
3 - Exibir quantas letras existem sem contar espaços
4 - Quantas letras tem o primeiro nome
'''

nome = str(input("Qual seu nome completo: ")).strip()

print("Seu nome com letras maiusculas: {}".format(nome.upper()))
print("Seu nome com letras minúsculas: {}".format(nome.lower()))
print("{} possui {} letras".format(nome, len(nome) - nome.count(' ')))
#print("Seu primeiro nome possui {} letras".format(nome.find(' ')))
print("Seu primeiro nome \"{}\" possui {} letras".format(nome.split()[0], len(nome.split()[0])))
