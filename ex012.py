# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço
# com 5% de desconto

valorOriginal = float(input("Informe o preço do produto: "))
porcentagemDesconto = 5;
valorDesconto = valorOriginal * (porcentagemDesconto / 100)

print("O valor atualizado do produto com {}% de desconto será: {:.2f}".format(porcentagemDesconto, valorOriginal-valorDesconto))


