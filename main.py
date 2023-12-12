import pygame as pg
from random import randrange
import pymunk.pygame_util
pymunk.pygame_util.positive_y_is_up = False

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
draw_options = pymunk.pygame_util.DrawOptions(surface)

# Настройки PyMunk
space = pymunk.Space()
space.gravity = 0, 900000

# Платформа
segment_shape = pymunk.Segment(space.static_body, (1, HEIGHT), (WIDTH, HEIGHT), 26)
space.add(segment_shape)
segment_shape.elasticity = 0.0
segment_shape.friction = 0.0

vertical_segment = pymunk.Segment(space.static_body, (0, 0), (0, HEIGHT), 100)
space.add(vertical_segment)
vertical_segment.collision_type = 3
vertical_segment.elasticity = 1.0
vertical_segment.friction = 0.0


# Квадратик 1
square1_moment = pymunk.moment_for_box(square1_mass, square1_size)
square1_body = pymunk.Body(square1_mass, square1_moment)

square1_body.position = (300, 620)
square1_shape = pymunk.Poly.create_box(square1_body,square1_size)
square1_shape.collision_type = 1
square1_shape.elasticity = 1.0
square1_shape.friction = 0.0
# цвет квадратика
square1_shape.color = [randrange(256) for i in range(4)]
# скорость квадратика
square1_body.apply_impulse_at_world_point(velocity1, square1_body.position)

square1_shape.group = 1

space.add(square1_body, square1_shape)

# Квадратик 2
square2_moment = pymunk.moment_for_box(square2_mass, square2_size)
square2_body = pymunk.Body(square2_mass, square2_moment)

square2_body.position = (570, 620)
square2_shape = pymunk.Poly.create_box(square2_body,square2_size)
square2_shape.collision_type = 2
square2_shape.elasticity = 1.0
square2_shape.friction = 0.0
# цвет квадратика
square2_shape.color = [randrange(256) for i in range(4)]
# скорость квадратика

square2_body.apply_impulse_at_world_point(velocity2, square2_body.position)

square2_shape.group = 2

space.add(square2_body, square2_shape)

countCollisions = 0

def collide(arbiter, space, data):
    global countCollisions
    countCollisions += 1
    print(countCollisions)

handler = space.add_collision_handler(1, 2)
handler2 = space.add_collision_handler(1, 3)
handler.post_solve = collide
handler2.post_solve = collide


# Отрисовка PyGame
while True:
    surface.fill(pg.Color('black'))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    space.step(1/FPS)
    space.debug_draw(draw_options)

    pg.display.flip()
    clock.tick(FPS*150)

