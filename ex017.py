# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo, calcule e mostre 
# o comprimento da hipotenusa.
from math import hypot

opo = float(input("Indique o comprimento do cateto oposto: "))
adj = float(input("Indique o comprimento do cateto adjacente: "))

# hip = ((adj ** 2) + (opo ** 2)) ** (1/2)
hip = hypot(opo, adj)

print("A hipotenusa do triângulo retângulo cujo cateto oposto mede {}".format(opo), end=" ")
print("e o cateto adjacente mede {} é igual à {:.3f}".format(adj, hip))
