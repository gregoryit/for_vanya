from turtle import *
a = input('Введите размер пера:')
t = Turtle()
t.color('black')
t.width(a)
t.shape('circle')
t.pendown()
t.speed(3999)
print('1 - зелёный , 2 - красный , 3 - желтый ,4 - синий , 5 - розовый , 6 - коричневый , 7 - чёрный         > вправо , < влево , ↑ вверх  , ↓ вниз , 0 - круг , w - размер 8 , s - размер 4 , e - начать заливку , q - закончить заливку ')

def draw(x ,y):
    t.goto(x, y)
def move(x, y):
    t.penup()
    t.goto(x , y)
    t.pendown()

def setGreen():
    t.color('green')

def setRed():
    t.color('red')

def setYellow():
    t.color('Yellow')


def setBlue():
    t.color('blue')

def setPink():
    t.color('#ff008c')

def setBrown():
    t.color('#964B00')

def setBlack():
    t.color('black')

def stepRight():
    t.goto(t.xcor() + 5, t.ycor())
def stepLeft():
    t.goto(t.xcor() - 5, t.ycor())
def stepUp():
    t.goto(t.xcor() , t.ycor() + 5)
def stepDown():
    t.goto(t.xcor() , t.ycor() - 5)
def stepCircle():
    t.circle(30)
def setW():
    t.width(8)
    
def setS():
    t.width(4)

def setBegin_fill():
    t.begin_fill()
def setEnd_fill():
    t.end_fill()


scr = t.getscreen()
scr.listen()
scr.onscreenclick(move)
scr.onkey(setBlack, '7')
scr.onkey(stepRight, 'Right')
scr.onkey(stepLeft, 'Left')
scr.onkey(setEnd_fill, 'q')
scr.onkey(setBegin_fill, 'e')
scr.onkey(setS, 's')
scr.onkey(stepCircle, '0')
scr.onkey(stepDown, 'Down')
scr.onkey(stepUp, 'Up')
scr.onkey(setW, 'w')
scr.onkey(setBrown, '6')
scr.onkey(setPink, '5')
scr.onkey(setYellow, '3')
scr.onkey(setRed, '2')
scr.onkey(setGreen, '1')
scr.onkey(setBlue, '4')
t.ondrag(draw)


