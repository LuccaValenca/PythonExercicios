# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta um área de 2m²

largura = float(input("Indique a largura da parede em metros: "))
altura = float(input("Indique a altura da parede em metros: "))

area = altura * largura
litrosNecessarios = area / 2

print("Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m².".format(largura, altura, area))
print("Você precisará de {:.2f} litros de tinta para pintar a parede.".format(litrosNecessarios))
