# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.

from pygame import mixer

mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.set_volume(1000)
mixer.music.play()
input('Agora você escuta?')
