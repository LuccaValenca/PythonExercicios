#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

print("Nota 1: {}\nNota 2: {}\n{}\nMédia: {:.1f}".format(nota1, nota2, '='*20, (nota1+nota2)/2))