# Faça um programa para abrir um auido de um arquivo mp3

# Opção 1 - Encontrei desta forma na internet
#import os
#os.startfile("C:\\Users\\Programacao\\Downloads\\Chaves.mp3")



# Opção 2 - Forma que o professor ensinou

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
#pygame.mixer.music.set_volume(15)
#pygame.event.wait(120)

import time
time.sleep(10)
