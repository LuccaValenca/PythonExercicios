# Programa que faça o PC pensar em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobri qual o número escolhido. O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
import emoji
from time import sleep

rand = randint(0, 5)
print("=*=*" * 18)
print("Tente adivinhar o número que pensei! Escolha um número de 0 à 5...")
print("=*=*" * 18)
num = int(input("Em que número eu pensei? "))
print("ANALISANDO...")
sleep(2)

if num == rand:
    print(emoji.emojize("Você venceu! O número escolhido pelo computador foi {} :star-struck:".format(rand)))
else:
    print(emoji.emojize("Não foi dessa vez :worried_face:"))
    print("Você escolheu {} e eu pensei em {}".format(num, rand))
    print(emoji.emojize("Continue tentando... :face_with_monocle:"))
