import pygame
from pygame.locals import * 
from sys import exit

pygame.init()

screen = pygame.display.set_mode((720,640))
pygame.display.set_caption("Desafio-Módulo 4")


while True:
    ret = pygame.draw.rect(screen, (0,0,0), [360,320,50,50])    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        x,y = pygame.mouse.get_pos()

        print(x,y)

    screen.fill((255,255,255))
    pressed_keys = pygame.key.get_pressed()
    key_direction = (0,0)
    if pressed_keys[K_LEFT]:
        key_direction.x = -1
    elif pressed_keys[K_RIGHT]:
        key_direction.x = +1
    if pressed_keys[K_UP]:
        key_direction.y = -1
    elif pressed_keys[K_DOWN]:
        key_direction.y = +1

    pygame.display.update()