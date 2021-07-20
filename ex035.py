# Leia três retas e verifique se pode ser um triângulo

r1 = float(input("Infique o comprimenro da primeira reta: "))
r2 = float(input("Indique o comprimento da segunda reta: "))
r3 = float(input("Indique o comprimento da terceira reta: "))

if ((r2 - r3) < r1 < (r2 + r3)) and ((r1 - r3) < r2 < (r1 + r3)) and ((r1 - r2) < r3 < (r1 + r2)):
    print("Dado os comprimentos das retas é possível formar um triângulo")
else:
    print("Dado os comprimentos das retas não é possível formar um triângulo")
