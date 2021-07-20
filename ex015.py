# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Informe a quantidade de KM percorridos com o veículo: "))
dias = int(input("Informe a quantidade de dias em que o veículo foi alugado: "))

total = (dias * 60) + (km * 0.15)

print("Após percorrer {}km durante os {} dias em que o veículo foi alugado, o valor total a ser pago é R${:.2f}".format(km, dias, total))