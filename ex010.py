bonoros = float(input("Quantos reais você possui atualmente: R$"))
cotacaoDolar = float(input("Qual a cotação do dolar atual: $"))

dolares = bonoros / cotacaoDolar;

print("Com o dolar à R${} você pode comprar {:.2f} dolares utilizando seus R${}".format(cotacaoDolar, dolares, bonoros))
