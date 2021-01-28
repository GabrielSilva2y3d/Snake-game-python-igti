import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'background.jpg'
logo_image_filename = 'logo.jpg'

pygame.init()

screen = pygame.display.set_mode((640,480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
logo = pygame.image.load(logo_image_filename)

clock = pygame.time.Clock()

x = 0

speed = 100

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    
    screen.blit(background, (0,0))
    screen.blit(logo,(x,100))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    distance_moved = time_passed_seconds * speed
    x += distance_moved

    if x > 640:
        x -= 640

    pygame.display.update()