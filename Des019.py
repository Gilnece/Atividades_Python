#Faça um programa em Python que abra e reproduza um arquivo de áudio MP3

import pygame
import time #mantem o programa aberto para não parar imediatamente ao começar a reproduzir
#inicializa o mixer
pygame.mixer.init()
#carrega a musica
pygame.mixer.music.load('Maneva - Luz que me traz paz.mp3')
#tocar a musica
pygame.mixer.music.play()
#Espera a música terminar de tocar
while pygame.mixer.music.get_busy():
    time.sleep(1)