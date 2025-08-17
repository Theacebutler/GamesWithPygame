# for game.py

import pygame as pg





HEIGHT = (300)
WIDTH = (300)
SNK_WIDTH = 25
SNK_START_HEIGHT = 25
BORDER_WIDTH = 0
STR_POS_W = 0
STR_POS_H = 0



FSP = 60
SNK_SPEED = 1



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)








def log(x):
    with open('log.txt', 'a') as log:
        log.write(str(x) + '\n================================\n')