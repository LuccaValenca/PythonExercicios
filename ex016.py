# Crie um programa que leia um número Real qualquer e mostre sua porção inteira.
from math import trunc

num = float(input("Informe um número real: "))
print("A parte inteira do número {} é {}. (math.trunc)".format(num, trunc(num)))
print("A parte inteira do número {} é {}. int".format(num, int(num)))
