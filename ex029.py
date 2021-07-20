# Leia a velocidade de um carro
# Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado
# O valor da multa é 7.00 por cada KM acima

vel = int(input("Indique a velocidade do veículo: "))

if vel > 80:
    multa = (vel - 80) * 7
    print("Você foi multado pelo limite de velocidade.")
    print("O valor da multa é R${:.2f} pelos {}km acima do permitido".format(multa, vel - 80))
else:
    print("Tenha um bom dia! Dirija com segurança!")
