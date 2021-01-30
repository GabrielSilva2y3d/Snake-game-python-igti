import turtle
import os

tela = turtle.Screen()
tela.title("jogo com turtle")
tela.bgcolor("white")
tela.setup(width=800,height=600)
tela.tracer(0)

#barra A
barra_A = turtle.Turtle()
barra_A.speed(1)
barra_A.shape('square')
barra_A.color('black')
barra_A.shapesize(stretch_wid=5,stretch_len=1)
barra_A.penup()
barra_A.goto(-350,0)

#barra B
barra_B = turtle.Turtle()
barra_B.speed(1)
barra_B.shape('square')
barra_B.color('red')
barra_B.shapesize(stretch_wid=5,stretch_len=1)
barra_B.penup()
barra_B.goto(350,0)

#bola 
bola = turtle.Turtle()
bola.speed()
bola.shape('square')
bola.color('gray')
bola.penup()
bola.goto(0,0)
#adcionando movimento
bola.dx = 1.0
bola.dy = 1.0

#atribuindo a pontuação
pontuacao_A = 0
pontuacao_B = 0

#desenhando o placar
placar = turtle.Turtle()
placar.speed()
placar.color('black')
placar.penup()
placar.hideturtle()
placar.goto(0,260)
placar.write(f"jogador A: {pontuacao_A}  jogador B: {pontuacao_B}",align='center', font = ("Courier", 24,"normal"))

#funções para movimento
#cima
def barra_A_cima():
    y = barra_A.ycor()
    y = y+20
    barra_A.sety(y)

#baixo
def barra_A_baixo():
    y = barra_A.ycor()
    y = y-20
    barra_A.sety(y)

#cima
def barra_B_cima():
    y = barra_B.ycor()
    y = y+20
    barra_B.sety(y)

#baixo
def barra_B_baixo():
    y = barra_B.ycor()
    y = y-20
    barra_B.sety(y)

#recebendo dados do teclado
tela.listen()
tela.onkeypress(barra_A_cima,"w")
tela.onkeypress(barra_A_baixo,"s")
tela.onkeypress(barra_B_cima,"Up")
tela.onkeypress(barra_B_baixo,"Down")

#loop Principal

while True:
    tela.update()

    #adicionando o movimento da bola
    bola.setx(bola.xcor()+bola.dx)
    bola.sety(bola.ycor()+bola.dy)

    #definindo as bordas
    if bola.ycor() > 290:
        bola.sety(290) 
        #reverte o movimento
        bola.dy = bola.dy*-1
    
    #definindo as bordas 
    if bola.ycor() < -290:
        bola.sety(-290) 
        #reverte o movimento
        bola.dy = bola.dy*-1

    if bola.xcor() > 390:
        bola.goto(0,0)
        bola.dx = bola.dx*-1
        pontuacao_A = pontuacao_A + 1 
        placar.clear()
        placar.write(f"jogador A: {pontuacao_A}  jogador B: {pontuacao_B}",align='center', font = ("Courier", 24,"normal"))

    if bola.xcor() < -390:
        bola.goto(0,0)
        bola.dx = bola.dx*-1
        pontuacao_B = pontuacao_B + 1 
        placar.clear()
        placar.write(f"jogador A: {pontuacao_A}  jogador B: {pontuacao_B}",align='center', font = ("Courier", 24,"normal"))


    if(bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < barra_B.ycor() + 40 and bola.ycor() > barra_B.ycor() - 40):
        bola.setx(340)
        bola.dx = bola.dx*-1

    if(bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < barra_A.ycor() + 40 and bola.ycor() > barra_A.ycor() - 40):
        bola.setx(-340)
        bola.dx = bola.dx*-1

    