import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'background.jpg'
logo_image_filename = 'logo.jpg'

pygame.init()

screen = pygame.display.set_mode((640,480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
logo = pygame.image.load(logo_image_filename)

#coordenada do logo
x = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    
    screen.blit(background,(0,0))
    screen.blit(logo,(x,100))
    x += 2

    #verifica se a imagem saiu da tela
    if x > 640:
        x -= 640

    pygame.display.update() 