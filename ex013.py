# Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento

salarioOriginal = float(input("Informe o valor original do salário: "))
porcentagemAumento = 15
salarioAumento = salarioOriginal + (salarioOriginal * (porcentagemAumento / 100))

print("O novo salario com aumento de {}% será {}".format(porcentagemAumento, salarioAumento))