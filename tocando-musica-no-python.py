import pygame
# iniciar o pygame
pygame.init()
# dentro das parenteses colocar a música
pygame.mixer.music.load('')
# tocar a música
pygame.mixer.music.play()
# criando evento para esperar a música terminar de tocar até fechar o programa
pygame.event.wait()
