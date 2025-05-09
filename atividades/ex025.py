import pygame

pygame.mixer.init()
pygame.mixer.music.load('c:/Users/André/Documents/GitHub/Python/atividades/audiopy.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)