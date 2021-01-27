import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Teste de cores')

branco = (255,255,255)
preto =     (0,0,0)
vermelho = (255,0,0)
verde =    (0,255,0)
azul =     (0,0,255)


#pygame.display.update()

game_exit = False

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

    #screen.fill(branco)
    #pygame.display.update()

pygame.quit()
quit()