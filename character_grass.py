from pico2d import *
import math

canvas_width = 800
canvas_height = 600
open_canvas(canvas_width, canvas_height)

character = load_image('character.png')
grass = load_image('grass.png')

x = 400
y = 90
turn = 1
theta = 0

def draw():
    clear_canvas()
    grass.draw_now(400, 30)
    character.draw_now(x, y)

while True:
    draw()

    # 사각형 움직이기
    if turn % 6 == 1:
        if x < canvas_width - 30:
            x += 6
        else:
            turn += 1
    elif turn % 6 == 2:
        if y < canvas_height - 60:
            y += 6
        else:
            turn += 1
    elif turn % 6 == 3:
        if x > 30:
            x -= 6
        else:
            turn += 1
    elif turn % 6 == 4:
        if y > 90:
            y -= 6
        else:
            turn += 1
    elif turn % 6 == 5:
        if x < 400:
            x += 6
        else:
            turn += 1


    # 원 움직이기
    elif turn % 6 == 0:
        theta += 2
        if theta >= 360:
            theta = 0
            turn = 1
        x = 400 -  340 * math.sin(math.radians(theta))
        y = 330 - 240 * math.cos(math.radians(theta))

    delay(0.01)

close_canvas()
