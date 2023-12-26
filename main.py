import pygame as pg
from random import randrange

square1_mass, square1_size = 1, (100, 100)
square2_mass, square2_size = 1000000, (150, 150)
velocity1 = (0, 0)
velocity2 = (-10*square2_mass, 0)

# Настройки PyGame
RES = WIDTH, HEIGHT = 970, 720
FPS = 120

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()

surface.fill(pg.Color('black'))

pg.display.flip()
clock.tick(FPS*150)
# Отрисовка PyGame
while True:

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()


