# Leia o salario de um funcionario e calcule seu aumento
# Para salaários superiores à 1250 aumento de 10%
# Para salários inferiores aumento de 15%

salario = float(input("Informe o valor do salário: "))
pc = 0.10

if salario < 1250:
    pc = 0.15

novosalario = salario + salario * pc

print("Seu novo salário é: R$ {:.2f} com um aumento de {:.0f}%".format(novosalario, pc * 100))
