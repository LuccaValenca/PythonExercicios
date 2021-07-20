# Leia um número e indique se é par ou impar

num = int(input("Digite um número: "))

if (num % 2) == 0:
    print("{} é um número par".format(num))
else:
    print("{} é um número ímpar".format(num))
