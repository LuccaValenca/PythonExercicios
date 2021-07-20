# Leia a distancia de uma viagem em KM e calcule o preço da passagem
# Cobrando 0.50 por KM para viagens até 200KM e 0.45 para viagens mais longas

distancia = int(input("Informe a distância da viagem em KM: "))
valor = distancia * 0.5 if distancia <= 200 else distancia * 0.45

print("O valor da viagem será de R${:.2f}".format(valor))
