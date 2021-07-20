# O mesmo professor do desafio anterior quer sortear a ordem
# de apresentacao de trabalhos dos alunos. Faça um programa
# que leia o nome dos 4 alunos e mostre a ordem sorteada.

from random import sample, shuffle

a1 = input("1° Aluno: ")
a2 = input("2° Aluno: ")
a3 = input("3° Aluno: ")
a4 = input("4° Aluno: ")
lista = [a1, a2, a3, a4]
shuffle(lista)

print("A ordem de apresentação será {}".format(lista))
# print("A ordem de apresentação será {}".format(sample(lista, k=4 )))

