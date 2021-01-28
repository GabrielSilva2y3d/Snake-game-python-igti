import pygame
from pygame.locals import *
from sys import exit
from random import randint

background_image_filename = 'background.jpg'
logo_image_filename = 'logo.png'
SCREEN_SIZE = (800,600)

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

background = pygame.image.load(background_image_filename).convert()
logo = pygame.image.load(logo_image_filename).convert_alpha()

clock = pygame.time.Clock()

x,y = 0,10
speed_x, speed_y = 500,500   

Fullscreen = False


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        
        if event.type == KEYDOWN:
            if event.key == K_f:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN,32)
                else:
                    screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

        if event.type == VIDEORESIZE:
            SCREEN_SIZE = event.size
            screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
            pygame.display.set_caption('Janela modificada para '+str(event.size))
        
        screen_width, screen_height = SCREEN_SIZE
        for y in range(0, screen_height, background.get_height()):
            for x in range(0, screen_width, background.get_width()):
                screen.blit(background, (x, y))

        
    screen.blit(background, (0,0))
    screen.blit(logo,(x,y))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    x += speed_x * time_passed_seconds
    y += speed_y * time_passed_seconds

    #distance_moved = time_passed_seconds * speed
    #x += distance_moved

    #verifica a posição do sprite
    if x > SCREEN_SIZE[0] - logo.get_width():
        speed_x = -speed_x
        x = SCREEN_SIZE[0] - logo.get_width()
    elif x < 0:
        speed_x = -speed_x
        x = 0

    if y > SCREEN_SIZE[1] - logo.get_height():
        speed_y = -speed_y
        y = SCREEN_SIZE[1] - logo.get_height()
    elif y < 0:
        speed_y = -speed_y
        y = 0
     
    
    for _ in range(25):
           random_color = (randint(0,255),randint(0,255),randint(0,255))
           random_pos = (randint(0,SCREEN_SIZE[0]),randint(0,SCREEN_SIZE[1]))
           random_radius = randint(1,200)
           pygame.draw.circle(screen,random_color,random_pos,random_radius)
    
    mouse_pos = pygame.mouse.get_pos()
    for x in range(0,SCREEN_SIZE[0],20):
        pygame.draw.line(screen, (0,255,255),(x,0),mouse_pos)
        pygame.draw.line(screen, (0,0,255),(x,(SCREEN_SIZE[1]-1)),mouse_pos)

    for y in range(0,SCREEN_SIZE[1],20):
        pygame.draw.line(screen, (255,0,0),(0,y),mouse_pos)
        pygame.draw.line(screen, (0,255,0),((SCREEN_SIZE[0]-1),y),mouse_pos)
    
    pygame.display.update()