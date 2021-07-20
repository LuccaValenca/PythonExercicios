#Leia um número de 0 à 9999 e mostre na tela cada um dos digiTos separados

num = int(input("Informe um número de 0 à 9999: "))

# não é possível ainda fazer por string sem laço
# n = str(num)
# print("Unidade: {}".format(n[3]))
# print("Dezena: {}".format(n[2]))
# print("Centena: {}".format(n[1]))
# print("Milhar: {}".format(n[0]))

print("\nMatematicamente\n")
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print("Unidade: {}".format(uni))
print("Dezena: {}".format(dez))
print("Centena: {}".format(cen))
print("Milhar: {}".format(mil))
