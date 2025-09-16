from pico2d import *
import math

open_canvas()

boy = load_image('character.png')


def move_top():
    print('Moving top')
    for x in range(0, 800, 5):
        draw_boy(x, 550)
    pass


def move_right():
    print('Moving right')
    pass


def move_bottom():
    print('Moving bottom')
    pass


def move_left():
    print('Moving left')
    pass


def move_rectangle():
    print("Move rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass


def move_circle():
    print("Move circle")
    r = 200
    for degree in range(0, 360):
        x = r * math.cos(math.radians(degree)) + 400
        y = r * math.sin(math.radians(degree)) + 300
        draw_boy(x, y)
    pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)


while True:
    move_circle()
    move_rectangle()
    #break

close_canvas()
