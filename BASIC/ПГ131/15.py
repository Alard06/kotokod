import pygame as pg

pg.init()


width, height = 1000, 800
screen = pg.display.set_mode((width, height))

pg.display.set_caption("GAME MEGA OVER GAME")

while True:
    for event in pg.event.get():
        # print(event)
        if event.type == 256:
            pg.quit()
            exit(0)
        if event.type == 1025:
            x, y = event.pos
            pg.draw.circle(screen, (255, 0, 0), (x, y), 10)

    pg.display.flip()

