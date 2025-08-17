import pygame as pg




WIDTH = 700
HEIGHT = 300

cat_height = 50
cat_width = 100
cat_speed = 1
cat_jump = 100

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)


cat = pg.Rect(WIDTH // 4, HEIGHT - cat_height, cat_width, cat_height)
