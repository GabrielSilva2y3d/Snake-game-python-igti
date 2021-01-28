import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'background.jpg'
SCREEN_SIZE = (800,600)
pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
background = pygame.image.load(background_image_filename).convert()

font = pygame.font.SysFont("arial", 32);
font_height = font.get_linesize()

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

    pressed_key_text = []
    pressed_keys = pygame.key.get_pressed()
    y = font_height

    for key_constant, pressed in enumerate(pressed_keys):
        if pressed:
            key_name = pygame.key.name(key_constant)
            text_surface = font.render(key_name + " pressinado", True,(255,255,255))
            screen.blit(text_surface,(50,y))
            y += font_height

    pygame.display.update() 