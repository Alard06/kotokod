import pygame as pg
import random

pg.init()

r = 0
g = 0
b = 0
radius = 0
width, height = 1000, 800
screen = pg.display.set_mode((width, height))

pg.display.set_caption("GAME MEGA OVER GAME")

while True:
    for event in pg.event.get():
        # print(event)
        if event.type == 256:
            pg.quit()
            exit(0)
        if event.type == 1024:
            x, y = event.pos
            btns = event.buttons
            if btns == (1, 0, 0):
                print("Button")
                pg.draw.circle(screen, (255, 255, 255), (x, y), radius)
            # if event.button == 4:
            #     radius += 1
            # if event.button == 5:
            #     radius -= 1
        if event.type == 768:
            id_key = event.key
            if id_key == pg.K_1:
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)

            if id_key == pg.K_2:
                radius += 1

    pg.display.flip()

