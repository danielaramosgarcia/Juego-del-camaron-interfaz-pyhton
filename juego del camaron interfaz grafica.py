#intento de graficar
import turtle
import time
import string
from turtle import *
from math import *
from random import *

screen = turtle.Screen()
camaron= turtle.Turtle()
obstaculob=turtle.Turtle()
obstaculom=turtle.Turtle()
pen = turtle.Turtle()
pen.hideturtle()
pen.pencolor('#111111')
pen.fillcolor('white')
x2,x3,y2,y3=0,0,0,0
posxb = -150
posybjugar = -50
posybinst= 200
posybsalir= -300
posybmenu=-470
largoboton = 300
anchoboton = 100
screen.bgcolor('pink')
mode = 'dark'
listaposiciones=[-300,-200,-100,0,100,200,300]
posobsb=[choice(listaposiciones),choice(listaposiciones),choice(listaposiciones),choice(listaposiciones),choice(listaposiciones),choice(listaposiciones)]
posobsm=[choice(listaposiciones),choice(listaposiciones),choice(listaposiciones),choice(listaposiciones),choice(listaposiciones),choice(listaposiciones)]

tamañocelda = 100 # pixels (default is 100)
numerocolumnas = 7 # cells (default is 7)
numerofilas = 7 # cells (default is 6)
margendex = tamañocelda * 2 # pixels, the size of the margin left/right of the board
margendey = tamañocelda // 2 # pixels, the size of the margin below/above the board
alturadecanvas = numerofilas * tamañocelda + margendey * 2 +200
anchodecanvas = numerocolumnas * tamañocelda + margendex * 2 

assert tamañocelda >= 80, 'Cells must be at least 80x80 pixels in size'
assert numerocolumnas >= 7, 'Board must be at least 7 columns wide'
assert numerofilas >= 7, 'Board must be at least 6 rows high'

setup(anchodecanvas, alturadecanvas)
bgcolor('pink')
turtle.color('white')
style=('Arial', 15, 'normal')
turtle.write(' ¡BIENVENID@!, ¿Cuál es tu nombre?', font=style, align='center')
nombre=""



def pasardecuadricula():
    camaron.color('red')
    time.sleep(0.5)
    camaron.color('green')
    presionarflechas()
    
def hacerobstaculos():
    obstaculom.pu()
    obstaculom.shape('square')
    obstaculom.shapesize(2,2,2)
    obstaculom.color('purple')
    obstaculob.shape('circle')
    obstaculob.shapesize(2,2,2)
    obstaculob.color('blue')
    obstaculob.pu()
    for i in range (3):
        obstaculob.goto(posobsb[i],posobsb[i+3])
        obstaculob.stamp()
        obstaculom.goto(posobsm[i],posobsm[i+3])
        obstaculom.stamp()

def moveralaizquierda():
    global x2
    global y2
    x2=camaron.xcor()
    y2=camaron.ycor()
    x2=x2-tamañocelda
    if x2<-301 or (x2==posobsm[0] and y2==posobsm[3]) or (x2==posobsm[1] and y2==posobsm[4]) or (x2==posobsm[2] and y2==posobsm[5]):
        pasardecuadricula()
    elif (x2==posobsb[0] and y2==posobsb[3]) or (x2==posobsb[1] and y2==posobsb[4]) or (x2==posobsb[2] and y2==posobsb[5]):
        if (x2-tamañocelda)<-301:
            pasardecuadricula()
        else:
            x2=x2-tamañocelda
            camaron.clearstamps()
            camaron.setx(x2)
            camaron.settiltangle(180)
            camaron.stamp()
            presionarflechas()
    else:
        camaron.clearstamps()
        camaron.setx(x2)
        camaron.settiltangle(180)
        camaron.stamp()
        presionarflechas()
    
def moveraladerecha():
    global x2
    global y2
    x2=camaron.xcor()
    y2=camaron.ycor()
    x2=x2+tamañocelda
    if x2>301 or (x2==posobsm[0] and y2==posobsm[3]) or (x2==posobsm[1] and y2==posobsm[4]) or (x2==posobsm[2] and y2==posobsm[5]):
        pasardecuadricula()
    elif (x2==posobsb[0] and y2==posobsb[3]) or (x2==posobsb[1] and y2==posobsb[4]) or (x2==posobsb[2] and y2==posobsb[5]):
        if (x2+tamañocelda)>301:
            pasardecuadricula()
        else:
            x2=x2+tamañocelda
            camaron.clearstamps()
            camaron.setx(x2)
            camaron.settiltangle(0)
            camaron.stamp()
            presionarflechas()
    else:
        camaron.clearstamps()
        camaron.setx(x2)
        camaron.settiltangle(0)
        camaron.stamp()    
        presionarflechas()
       
def moverarriba():
    global x2
    global y2
    y2=camaron.ycor()
    x2=camaron.xcor()
    y2=y2+tamañocelda
    if y2>301 or (x2==posobsm[0] and y2==posobsm[3]) or (x2==posobsm[1] and y2==posobsm[4]) or (x2==posobsm[2] and y2==posobsm[5]):
        pasardecuadricula()
    elif (x2==posobsb[0] and y2==posobsb[3]) or (x2==posobsb[1] and y2==posobsb[4]) or (x2==posobsb[2] and y2==posobsb[5]):
        if (y2+tamañocelda)>301:
            pasardecuadricula()
        else:
            y2=y2+tamañocelda
            camaron.clearstamps()
            camaron.sety(y2)
            camaron.settiltangle(90)
            camaron.stamp()
            presionarflechas()
    else:
        camaron.clearstamps()
        camaron.sety(y2)
        camaron.settiltangle(90)
        camaron.stamp()    
        presionarflechas()
 
def moverabajo():
    global x2
    global y2
    y2=camaron.ycor()
    x2=camaron.xcor()
    y2=y2-tamañocelda
    if y2<-301 or (x2==posobsm[0] and y2==posobsm[3]) or (x2==posobsm[1] and y2==posobsm[4]) or (x2==posobsm[2] and y2==posobsm[5]):
        pasardecuadricula()
    elif (x2==posobsb[0] and y2==posobsb[3]) or (x2==posobsb[1] and y2==posobsb[4]) or (x2==posobsb[2] and y2==posobsb[5]):
        if (y2-tamañocelda)<-301:
            pasardecuadricula()
        else:
            y2=y2-tamañocelda
            camaron.clearstamps()
            camaron.sety(y2)
            camaron.settiltangle(270)
            camaron.stamp()
            presionarflechas()
    else:
        camaron.clearstamps()
        camaron.sety(y2)
        camaron.settiltangle(270)
        camaron.stamp()
        presionarflechas()
    
def presionarflechas():
    if x2==x3 and y2==(y3+25):
        pen.clear()
        camaron.clear()
        camaron.ht()
        obstaculob.clear()
        obstaculom.clear()
        obstaculob.ht()
        obstaculom.ht()
        screen.tracer(0)
        pen.color("black")
        pen.penup()
        pen.begin_fill()
        pen.goto(-150,150)
        pen.goto(150,150)
        pen.goto(150,-50)
        pen.goto(-150,-50)
        pen.goto(-150,150)
        pen.end_fill()
        pen.goto(-130,-10)
        pen.color("white")
        pen.write("""     
    ¡¡FELICIDADES
           """+ nombre.upper()+"""
        GANASTE!!""", font = ('Arial', 15, 'normal'))
        screen.update()
        time.sleep(2)
        screen.bye()
    camaron.pu()
    screen.listen()
    screen.onkeypress(moveralaizquierda,"Left")
    screen.onkeypress(moveraladerecha,"Right")
    screen.onkeypress(moverarriba,"Up")
    screen.onkeypress(moverabajo,"Down")
    
def hacermeta():
    screen.tracer(0)
    global x3
    global y3
    x3,y3=choice(listaposiciones),choice(listaposiciones)-25
    pen.goto(x3,y3)
    pen.fillcolor('black')
    pen.begin_fill()
    pen.left(140)
    pen.forward(40)
    for i in range(12):
        pen.right(16)
        pen.forward(5)
    pen.left(125)
    for i in range(12):
        pen.right(16)
        pen.forward(5)
    pen.right(15)
    pen.forward(40)
    pen.end_fill()
    pen.up()
    pen.goto(x3-18,y3+24)
    pen.down()
    pen.color('white')
    pen.write("Meta", font=(
      "Verdana", 7, "bold"))
    screen.update()
    screen.tracer(1)
    
def hacercursor():
    camaron.shapesize(2.5,2.5,2.5)
    camaron.shape('turtle')
    camaron.color('green')
    camaron.goto(choice(listaposiciones),choice(listaposiciones))
    camaron.stamp()

def hacercuadricula(mark_legend_spaces = False, # show text for legend
                          mark_axes = True, # show labels on axes
                          bg_colour = 'white', # background colour
                          line_colour = 'pink'): # line colour for board
    turtle.clear()   
    setup(anchodecanvas, alturadecanvas)
    bgcolor(bg_colour)
    tracer(False)
    penup()
    color(line_colour)
    width(3.5)
    limiteizq = -(numerocolumnas * tamañocelda) // 2 
    limiteabajo = -(numerofilas * tamañocelda) // 2
    limitearriba=(numerofilas * tamañocelda) // 2
    setheading(0) # face east
    for line_no in range(0, numerofilas + 1):
        penup()
        goto(limiteizq, limiteabajo + line_no * tamañocelda)
        pendown()
        forward(numerocolumnas * tamañocelda)
    setheading(90) # face north
    for line_no in range(0, numerocolumnas + 1):
        penup()
        goto(limiteizq + line_no * tamañocelda, limiteabajo)
        pendown()
        forward(numerofilas * tamañocelda)
    penup()
    
    if mark_axes:
        small_font = ('Arial', (18 * tamañocelda) // 100, 'normal')
        y_offset = (27 * tamañocelda) // 100 # pixels
        penup()
        turtle.color('pink')
        for x_label in range(0, numerocolumnas):
            goto(limiteizq + (x_label * tamañocelda) + (tamañocelda // 2), limitearriba)
            write(str(x_label + 1), align = 'center', font = small_font)
        goto(limiteizq + (3 * tamañocelda) + (tamañocelda // 2), limitearriba+50)
        turtle.color('black')
        style=('Arial', 20, 'italic')
        turtle.write("Juego del camarón",font=style, align="center")
        turtle.color('pink')
        penup()
        x_offset, y_offset = 7, 10 # pixels
        for y_label in range(0, numerofilas):
            goto(limiteizq - x_offset, limiteabajo + (y_label * tamañocelda) + (tamañocelda // 2) - y_offset)
            write(str(y_label + 1), align = 'right', font = small_font)
    penup()
    hacerobstaculos()
    home()
    pen.penup()
    pen.fillcolor('pink')
    pen.pencolor('white')
    pen.begin_fill()
    pen.goto(posxb, posybmenu)
    pen.goto(posxb + largoboton, posybmenu)
    pen.goto(posxb + largoboton, posybmenu + anchoboton)
    pen.goto(posxb, posybmenu + anchoboton)
    pen.goto(posxb, posybmenu)
    pen.end_fill()
    pen.goto(posxb + 110, posybmenu + 30)
    message='Menú'
    pen.write(message, font = ('Arial', 20, 'normal'))
    screen.onclick(botonmenujugar)
    pen.ht()
    camaron.pu()
    obstaculob.pu()
    obstaculom.pu()
    tracer(True)
    hacermeta()
    hacercursor()
    presionarflechas()    
    
def botonmenujugar(x, y):
    global mode
    if posxb <= x <= posxb + largoboton:
        if posybmenu <= y <= posybmenu + anchoboton:
            pen.clear()
            camaron.clear()
            camaron.ht()
            obstaculob.clear()
            obstaculom.clear()
            obstaculob.ht()
            obstaculom.ht()
            iniciodeljuego()   
  
def botonmenu(x, y):
    global mode
    if posxb <= x <= posxb + largoboton:
        if posybsalir <= y <= posybsalir + anchoboton:
            pen.clear()   
            iniciodeljuego()    

def hacerinstrucciones(bg_colour = 'white'):
    turtle.clear()   
    setup(anchodecanvas, alturadecanvas)
    bgcolor(bg_colour)
    tracer(False)
    pen.pencolor('pink')
    goto(0,0)
    turtle.color('pink')
    style=('Arial', 15, 'normal')
    turtle.write('''                            ¡Bienvenid@ '''+ nombre+''' al Juego del Camaron!



                               El juego es sencillo ¡te vas a divertir!
                 Tu eres la tortuga y te puedes mover con las flechas de
                    tu teclado (derecha, izquierda, arriba y abajo).
             Tu objetivo es llegar a la meta la cual es un corazón color
        negro, pero ¡CUIDADO!, Tendrás obstaculos; los cuadrados no
             los podrás saltar y tendrás que rodearlos pero los circulos
                                         si los podrás saltar.
                                                      ¡Diviertete!''',font= style, align='center')
    pen.penup()
    pen.fillcolor('pink')
    pen.pencolor('white')
    pen.begin_fill()
    pen.goto(posxb, posybsalir)
    pen.goto(posxb + largoboton, posybsalir)
    pen.goto(posxb + largoboton, posybsalir + anchoboton)
    pen.goto(posxb, posybsalir + anchoboton)
    pen.goto(posxb, posybsalir)
    pen.end_fill()
    pen.goto(posxb + 110, posybsalir + 30)
    message='Menú'
    pen.write(message, font = ('Arial', 20, 'normal'))
    screen.onclick(botonmenu)

def botondeinst(pen, message = 'Instrucciones'):
    pen.pencolor('black')
    pen.fillcolor('white')
    pen.penup()
    pen.begin_fill()
    pen.goto(posxb, posybinst)
    pen.goto(posxb + largoboton, posybinst)
    pen.goto(posxb + largoboton, posybinst + anchoboton)
    pen.goto(posxb, posybinst + anchoboton)
    pen.goto(posxb, posybinst)
    pen.end_fill()
    pen.goto(posxb + 30, posybinst + 30)
    pen.write(message, font = ('Arial', 20, 'normal'))

def botondejugar(pen, message = 'Jugar'):
    pen.pencolor('black')
    pen.fillcolor('white')    
    pen.penup()
    pen.begin_fill()
    pen.goto(posxb, posybjugar)
    pen.goto(posxb + largoboton, posybjugar)
    pen.goto(posxb + largoboton, posybjugar + anchoboton)
    pen.goto(posxb, posybjugar + anchoboton)
    pen.goto(posxb, posybjugar)
    pen.end_fill()
    pen.goto(posxb + 100, posybjugar + 30)
    pen.write(message, font = ('Arial', 20, 'normal'))

def botondesalir(pen, message = 'Salir'):
    pen.pencolor('black')
    pen.fillcolor('white')
    pen.penup()
    pen.begin_fill()
    pen.goto(posxb, posybsalir)
    pen.goto(posxb + largoboton, posybsalir)
    pen.goto(posxb + largoboton, posybsalir + anchoboton)
    pen.goto(posxb, posybsalir + anchoboton)
    pen.goto(posxb, posybsalir)
    pen.end_fill()
    pen.goto(posxb + 110, posybsalir + 30)
    pen.write(message, font = ('Arial', 20, 'normal'))

def botonesprincipales(x, y):
    global mode
    if posxb <= x <= posxb + largoboton:
        if posybinst <= y <= posybinst + anchoboton:
            pen.ht()
            pen.clear()
            hacerinstrucciones()
    if posxb <= x <= posxb + largoboton:
        if posybjugar <= y <= posybjugar + anchoboton:
            pen.ht()
            pen.clear()
            hacercuadricula()
    if posxb <= x <= posxb + largoboton:
        if posybsalir <= y <= posybsalir + anchoboton:
            pen.ht()   
            screen.bye()
            
def iniciodeljuego():
    camaron.clear()
    turtle.clear()
    bgcolor('pink')
    turtle.color('white')
    tracer(False)
    botondeinst(pen)
    botondejugar(pen)
    botondesalir(pen)
    screen.onclick(botonesprincipales)    
    
def main(): 
    font = ("Courier", 25)
    turtle.pu()
    turtle.goto(-35,-80)

    def esc(key):
        global nombre
        turtle.write(key, font=font)
        turtle.forward(font[1]*1)
        nombre+=key

    def carriage_return():
        iniciodeljuego()

    all_characters = string.ascii_letters + string.punctuation 
    for key in all_characters:
        screen.onkeypress(lambda key=key: esc(key), key)

    screen.onkeypress(carriage_return, "Return")
    screen.listen()

main()