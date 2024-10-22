import pygame as pg
import sys
from random import randrange


class Game:
    def __init__(self):
        pg.init()
        self.WIDTH, self.HEIGHT = 1200, 700
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption("Breakout")
        self.paddle = Paddle(self)
        self.ball = Ball(self)
        self.FPS = 60
        self.clock = pg.time.Clock()

        # img
        self.image = pg.image.load("bg (1).jpg").convert()

        # blocs
        self.block_list = [
            pg.Rect(10 + 120 * i,
                    10 + 70 * j,
                    100,
                    50) for i in range(10) for j in range(4)
        ]
        self.color_list = [(randrange(30,  256),
                            randrange(30, 256),
                            randrange(30, 256)) for _ in range(10) for _ in range(4)]

    def run(self):
        while True:
            self.check_game_over()
            self.check_event()
            self.update()
            self.draw()

    def update(self):
        self.paddle.update()
        self.ball.update()
        pg.display.flip()
        self.clock.tick(self.FPS)

    def draw(self):
        self.screen.blit(self.image, (0, 0))
        for color, block in enumerate(self.block_list):
            pg.draw.rect(self.screen, self.color_list[color], block)
        self.paddle.draw()
        self.ball.draw()

    @staticmethod
    def check_event():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def check_game_over(self):
        pass

class Paddle:
    def __init__(self, root: Game):
        self.game = root
        self.paddle_w = 250
        self.paddle_h = 30
        self.paddle_speed = 15
        self.rect = pg.Rect(root.WIDTH // 2 - self.paddle_w // 2, root.HEIGHT - self.paddle_h - 10,
                            self.paddle_w, self.paddle_h)
        self.color = pg.Color(200, 135, 34)

    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_LEFT] and self.rect.left > 0:
            self.rect.left -= self.paddle_speed
        if key[pg.K_RIGHT]:
            print('K_RIGHT')

    def draw(self):
        pg.draw.rect(self.game.screen, self.color, self.rect)


class Ball:
    def __init__(self, root: Game):
        self.game = root
        self.radius = 20
        self.speed = 6

        self.rect = int(self.radius * 2 ** 0.5)
        self.ball = pg.Rect(randrange(self.rect, self.game.WIDTH-self.rect), self.game.HEIGHT // 2, self.rect,self.rect)
        self.dx, self.dy = 1, -1

    def update(self):
        self.move()

    def move(self):
        self.ball.x += self.speed * self.dx
        self.ball.y += self.speed * self.dy


    def draw(self):
        pg.draw.circle(self.game.screen, pg.Color(255, 255, 255), self.ball.center, self.radius)



if __name__ == '__main__':
    game = Game()
    game.run()
