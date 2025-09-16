from pico2d import *
import math

# 기본 캔버스 (기본 pico2d 예제는 800x600)
open_canvas(800, 600)

boy = load_image('character.png')
grass = load_image('grass.png')

# 경계 값 (캐릭터가 테두리 밖으로 나가지 않도록 설계된 이동 경로)
LEFT = 30
RIGHT = 770
BOTTOM = 60   # 잔디 위 여유 높이
TOP = 550

FRAME_DELAY = 0.01


def draw_scene(x: float, y: float):
    clear_canvas()
    # 잔디는 바닥 중앙 (원본 예제와 동일하게 400, 0)
    grass.draw(400, 0)
    # 경계 클램프 (혹시 계산 중 살짝 벗어나는 경우 보정)
    cx = max(LEFT, min(RIGHT, x))
    cy = max(BOTTOM, min(TOP, y))
    boy.draw(cx, cy)
    update_canvas()
    delay(FRAME_DELAY)


# ---------------- 사각형 운동 -----------------
def move_rectangle():
    # 아래 -> 위 방향: LEFT->RIGHT, TOP, RIGHT->LEFT, BOTTOM 순서(시계 or 반시계 선택)
    # 여기서는 반시계(위쪽 왼->오, 오른쪽 위->아래, 아래쪽 오->왼, 왼쪽 아래->위)
    # 상단 직선
    for x in range(LEFT, RIGHT + 1, 5):
        draw_scene(x, TOP)
    # 오른쪽 세로
    for y in range(TOP, BOTTOM - 1, -5):
        draw_scene(RIGHT, y)
    # 하단 직선
    for x in range(RIGHT, LEFT - 1, -5):
        draw_scene(x, BOTTOM)
    # 왼쪽 세로
    for y in range(BOTTOM, TOP + 1, 5):
        draw_scene(LEFT, y)


# --------------- 삼각형 운동 --------------------
# 삼각형 꼭짓점: 좌하(LEFT,BOTTOM), 중앙상((LEFT+RIGHT)/2, TOP), 우하(RIGHT,BOTTOM)
VX1 = LEFT
VY1 = BOTTOM
VX2 = (LEFT + RIGHT) / 2
VY2 = TOP
VX3 = RIGHT
VY3 = BOTTOM


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def move_line(x1, y1, x2, y2, steps=120):
    for i in range(steps + 1):
        t = i / steps
        draw_scene(lerp(x1, x2, t), lerp(y1, y2, t))


def move_triangle():
    move_line(VX1, VY1, VX2, VY2)
    move_line(VX2, VY2, VX3, VY3)
    move_line(VX3, VY3, VX1, VY1)


# ---------------- 원 운동 ----------------------
# 중심을 사각형 안쪽에 두고 반지름이 경계를 넘지 않게 설정
CIRCLE_CENTER_X = (LEFT + RIGHT) / 2  # 400
CIRCLE_CENTER_Y = (BOTTOM + TOP) / 2   # 305 근처
RADIUS = min((RIGHT - LEFT), (TOP - BOTTOM)) * 0.35  # 여유 있는 반지름


def move_circle():
    # 0~359도 이동
    for degree in range(0, 360, 2):
        rad = math.radians(degree)
        x = CIRCLE_CENTER_X + RADIUS * math.cos(rad)
        y = CIRCLE_CENTER_Y + RADIUS * math.sin(rad)
        draw_scene(x, y)


def main_loop():
    while True:
        move_rectangle()
        move_triangle()
        move_circle()


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        pass
    finally:
        close_canvas()

