import pygame
import random
import math
import tkinter as tk
from tkinter import messagebox 

pygame.init()

class cubo(object):
    linhas = 20
    largura = 500
    def __init__(self,start, direcx=1,direcy=1,cor=(255,0,0)):
        self.pos = start
        self.direcx = 1
        self.direcy = 0
        self.color = cor

    def move(self, direcx, direcy):
        self.direcx = direcx
        self.direcy = direcy
        self.pos = (self.pos[0] + self.direcx, self.pos[1] + self.direcy)

    def desenhe(self, superficie, olhos = False):
        distancia = self.largura // self.linhas
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(superficie, self.color,(i* distancia + 1, j * distancia + 1, distancia - 2, distancia - 2))

        if olhos:
            centro = distancia // 2
            radius = 3
            meioCirculo = (i * distancia + centro - radius, j * distancia + 8) 
            meioCirculo2 = (i * distancia + distancia - radius * 2, j * distancia + 8)
            
            pygame.draw.circle(superficie, (0,0,0), meioCirculo, radius)
            pygame.draw.circle(superficie, (0,0,0), meioCirculo2, radius)


class cobra(object):
    corpo = []
    movimentos = {}

    def __init__(self, cor, posicao):
        self.cor = cor
        self.cabeca = cubo(posicao)
        self.corpo.append(self.cabeca)
        self.direcx = 0
        self.direcy = 1
    
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            teclas = pygame.key.get_pressed()

            for tecla in teclas:
                
                if teclas[pygame.K_LEFT]:
                    self.direcx = -1
                    self.direcy = 0
                    self.movimentos[self.cabeca.pos[:]] = [self.direcx, self.direcy]
                
                elif teclas[pygame.K_RIGHT]:
                    self.direcx = 1
                    self.direcy = 0
                    self.movimentos[self.cabeca.pos[:]] = [self.direcx, self.direcy]
                
                elif teclas[pygame.K_UP]:
                    self.direcx = 0
                    self.direcy = -1
                    self.movimentos[self.cabeca.pos[:]] = [self.direcx, self.direcy]

                elif teclas[pygame.K_DOWN]:
                    self.direcx = 0
                    self.direcy = 1
                    self.movimentos[self.cabeca.pos[:]] = [self.direcx, self.direcy]
        
        for i, c in enumerate(self.corpo):
            p = c.pos[:]
            if p in self.movimentos:
                mova = self.movimentos[p]
                c.move(mova[0], mova[1])
                if i == len(self.corpo) - 1:
                    self.movimentos.pop(p)
            
            else:
                if c.direcx == -1 and c.pos[0] <= 0:
                    c.pos = (c.linhas - 1, c.pos[1])
                
                elif c.direcx == 1 and c.pos[0] >= c.linhas - 1: c.pos = (0,c.pos[1])
                
                elif c.direcy == 1 and c.pos[1] >= c.linhas-1: c.pos = (c.pos[0], 0)

                elif c.direcy == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.linhas - 1)

                else: c.move(c.direcx, c.direcy)

    
    def recomecar(self, posicao):
        self.cabeca = cubo(posicao)
        self.corpo = []
        self.corpo.append(self.cabeca)
        self.movimentos = {}
        self.direcx = 0
        self.direcy = 1

    
    def adicione_cubo(self):
        cauda = self.corpo[-1]
        dx, dy = cauda.direcx, cauda.direcy

        if dx == 1 and dy ==0:
            self.corpo.append(cubo((cauda.pos[0]-1, cauda.pos[1])))

        elif dx == -1 and dy == 0:
            self.corpo.append(cubo((cauda.pos[0]+1,cauda.pos[1])))

        elif dx == 0 and dy == 1:
            self.corpo.append(cubo((cauda.pos[0], cauda.pos[1]-1)))

        elif dx == 0 and dy == -1:
            self.corpo.append(cubo((cauda.pos[0], cauda.pos[1]+1)))

        
        self.corpo[-1].direcx = dx
        self.corpo[-1].direxy = dy
    
    def desenhe(self, superficie):
        for i, c in enumerate(self.corpo):
            if i == 0:
                c.desenhe(superficie, True)
            else:
                c.desenhe(superficie)
        
def desenheGrid(w, linhas, superficie):
    tamanho_entre = w // linhas
    x = 0
    y = 0

    for l in range(linhas):
        x = x + tamanho_entre
        y = y + tamanho_entre

        pygame.draw.line(superficie, (255,255,255), (x,0),(x,w))
        pygame.draw.line(superficie,(255,255,255), (0,y),(w,y))

def redesenheJanela(superficie):
    global linhas, largura, s, comida

    superficie.fill((0,0,0))

    s.desenhe(superficie)
    comida.desenhe(superficie)
    desenheGrid(largura,linhas,superficie)

    pygame.display.update()

def randomSnack(rows, item):

    posicoes = item.corpo

    while True:
        x = random.randrange(linhas)

        y = random.randrange(linhas)

        if len(list(filter(lambda z:z.pos == (x,y),posicoes))) > 0:
            continue
        else:
            break
    
    return(x ,y)

def message_box(assunto, conteudo):
    raiz = tk.Tk()
    raiz.attributes("-topmost", True)
    raiz.withdraw()
    messagebox.showinfo(assunto, conteudo)

    try:
        raiz.destroy()
    except:
        pass

def main():
    global largura, linhas, s, comida

    largura = 500
    linhas = 20

    janela = pygame.display.set_mode((largura,largura))

    s = cobra((255,0,0), (10,10))

    comida = cubo(randomSnack(linhas,s), cor = (0,255,0))

    bandeira = True

    clock = pygame.time.Clock()

    while bandeira:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()

        if s.corpo[0].pos == comida.pos:
            s.adicione_cubo()
            comida = cubo(randomSnack(linhas,s),cor = (0,255,0))
        
        for x in range(len(s.corpo)):
            if s.corpo[x].pos in list(map(lambda z:z. pos, s.corpo[x+1:])):
                print("\'Pontuação\'", len(s.corpo))

                message_box("\'You Lose!\'", "\'Try Again \'")

                s.recomecar((10,10))
                break
        
        redesenheJanela(janela)
main()


            



    
