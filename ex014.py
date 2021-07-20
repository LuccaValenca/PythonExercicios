# Escreva um programa que converta uma temperatura digitando em graus Celsius e
# converta para graus Fahrenheit.

celsius = float(input("Informe a temperatura em graus celsius: "))
fahrenheit = celsius * 1.8 + 32

print("{:.1f}° C equivale à {:.1f}° F".format(celsius, fahrenheit))