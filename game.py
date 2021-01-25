#introdução ao pygame
import pygame
from pygame.locals import *
from sys import exit

mouse_image_filename = 'mouse.png'
background_image_filename = 'background.jpg'

#Inicializando o console
pygame.init()

#definindo a tela
screen = pygame.display.set_mode((720,600))

#adicionando um nome para a tela
pygame.display.set_caption("Olá, Mundo Game!")

#definindo a imagem de background e converte para o mesmo formato do display
background = pygame.image.load(background_image_filename).convert()

#definindo a imagem do cursor (convert_alpha permite que as formas sejam desenhadas)
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

while True:

    for event in pygame.event.get(): #loop infinito que fica esperando o evento quit (clique no X da janela)
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        screen.blit(background, (0,0)) #coloca o background na tela

        x, y = pygame.mouse.get_pos() #obtem as posições do mouse na tela

        #coloca a imagem como o centro do cursor do mouse
        x-= mouse_cursor.get_width()/2
        y-= mouse_cursor.get_height()/2

        #coloca o cursor com a imagem na tela
        screen.blit(mouse_cursor, (x, y))

        #realiza o upgrade da tela
        pygame.display.update()