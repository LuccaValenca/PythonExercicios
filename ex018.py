# Faça um programa que leia um ângulo qualquer e mostre na
# tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angOriginal = float(input("Indique o valor do ângulo: "))
angRadiano = radians(angOriginal)

print("Para o ângulo de {}° temos:".format(angOriginal))
print("=="*15)
print("Seno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}".format(sin(angRadiano), cos(angRadiano), tan(angRadiano)))
