from pico2d import *
import math

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')

def move_top():
    print('Moving top')
    for x in range(30, 770, 5):
        draw(x, 550)
    pass


def move_right():
    print('Moving right')
    for y in range(550, 60, -5):
        draw(770, y)
    pass


def move_bottom():
    print('Moving bottom')
    for x in range(770, 30, -5):
        draw(x, 60)
    pass


def move_left():
    print('Moving left')
    for y in range(60, 550, 5):
        draw(30, y)
    pass


def draw(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    grass.draw_now(400,0)
    delay(0.01)

def move_rectangle():
    print("Move rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass

def move_triangle():
    print("Move triangle")
    # 가로 800 세로 600 바닥 60
    move_point1()
    move_point2()
    move_point3()
    pass


def move_point1():
    x = 30
    y = 60
    while y < 550 and x < 400:
        x += 370 / 97
        y += 490 / 97
        draw(x,y)
    pass
def move_point2():
    x = 400
    y = 550
    while y > 60 and x < 770:
        x += 370 / 97
        y -= 490 / 97
        draw(x, y)
    pass
def move_point3():
    x = 770
    while x > 30:
        x -= 740 / 147
        draw(x, 60)
    pass

def move_circle():
    print("Move circle")
    r = 200
    for degree in range(0, 360):
        x = r * math.cos(math.radians(degree)) + 400
        y = r * math.sin(math.radians(degree)) + 300
        draw(x, y)
    pass

while True:
    #move_rectangle()
    move_triangle()
    #move_circle()

    #break

close_canvas()
