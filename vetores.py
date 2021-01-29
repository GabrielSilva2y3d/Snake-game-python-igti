import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2

background_image_filename = 'background.jpg'
logo_image_filename = 'logo.png'
SCREEN_SIZE = (800,600)

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

background = pygame.image.load(background_image_filename).convert()
logo = pygame.image.load(logo_image_filename).convert_alpha()

clock = pygame.time.Clock()

logo_pos = Vector2(200,100)
logo_speed = 300

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    
        if event.type == VIDEORESIZE:
            SCREEN_SIZE = event.size
            screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
            pygame.display.set_caption('Janela modificada para '+str(event.size))
        
        screen_width, screen_height = SCREEN_SIZE
        for y in range(0, screen_height, background.get_height()):
            for x in range(0, screen_width, background.get_width()):
                screen.blit(background, (x, y))

    
    pressed_keys = pygame.key.get_pressed()
    key_direction = Vector2(0,0)

    if pressed_keys[K_LEFT]:
        key_direction.x = -1
    elif pressed_keys[K_RIGHT]:
        key_direction.x = +1
    if pressed_keys[K_UP]:
        key_direction.y = -1
    elif pressed_keys[K_DOWN]:
        key_direction.y = +1
    
    key_direction.normalize()

    screen.blit(background, (0,0))
    screen.blit(logo,(logo_pos.x,logo_pos.y))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    logo_pos += key_direction * logo_speed * time_passed_seconds

    pygame.display.update()