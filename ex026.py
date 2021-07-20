'''
Leia uma frase e apresente:

1 - Quantas vezes aparece a letra "A"
2 - Em que posição ela aparece pela primeira vez
3 - Em que posição ela aparece pela última vez
'''

frase = str(input("Digite uma frase: ")).strip()

print("Esta frase possui {} letras \"A\", ela aparece primeiro na posição {} e por último na posição {}".format(
    frase.upper().count('A'),
    frase.upper().find("A")+1,
    frase.upper().rfind('A')+1))
