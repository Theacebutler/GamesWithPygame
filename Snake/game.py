import pygame as pg
from utils import *
# make a board
# logic for win
# snake



BRD = pg.display.set_mode((HEIGHT, WIDTH))
SNK = pg.Rect(STR_POS_W, STR_POS_H, SNK_WIDTH, SNK_START_HEIGHT)


# border's
BORDER_TOP_T = pg.Rect(0,0, WIDTH,BORDER_WIDTH)
BORDER_TOP_B = pg.Rect(0,HEIGHT-BORDER_WIDTH, WIDTH,BORDER_WIDTH)
BORDER_SIDE_L = pg.Rect(0,0, BORDER_WIDTH,HEIGHT)
BORDER_SIDE_R = pg.Rect(WIDTH - BORDER_WIDTH,0, BORDER_WIDTH,HEIGHT)

pg.display.set_caption('Snake')



def change_movment(key):
    if key == pg.K_LEFT: SNK.x -= SNK_SPEED # go left
    if key == pg.K_RIGHT: SNK.x += SNK_SPEED # go right
    if key == pg.K_DOWN: SNK.y += SNK_SPEED # go down
    if key == pg.K_UP: SNK.y -= SNK_SPEED # go up







def game():
    in_game = True
    clock = pg.time.Clock()
    while in_game:
        clock.tick(FSP)
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                in_game = False


        BRD.fill(GREEN)
        pg.draw.rect(BRD, YELLOW, SNK)

        if ev.type == pg.KEYDOWN:
            change_movment(ev.key)


        # listen for hiting the border
        if SNK.x <= -1:
            SNK.x += SNK_SPEED

        elif SNK.x + SNK_WIDTH >= WIDTH +1:
            SNK.x -= SNK_SPEED

        elif SNK.y <= -1:
            SNK.y += SNK_SPEED

        elif SNK.y + SNK_START_HEIGHT >= HEIGHT +1:
            SNK.y -= SNK_SPEED




        pg.display.update()
