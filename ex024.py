# Leia o nome de uma cidade e indique se ela começa ou não com "SANTO"

cidade = str(input("Informe o nome da cidade: ")).strip()

print("{} {} com \"SANTO\"".format(cidade, str("SANTO" in cidade.upper().split()[0])).replace("True", "começa").replace("False", "não começa"))
print("{} {} com \"SANTO\"".format(cidade, str(cidade[:5].upper() == "SANTO")).replace("True", "começa").replace("False", "não começa"))

