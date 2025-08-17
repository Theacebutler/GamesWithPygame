import pygame as pg

from utils import *

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Jump')



def game():
    GameOpen = True

    while GameOpen:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                GameOpen = False
        
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    cat.y -= cat_jump
            else:
                cat.y = HEIGHT - cat_height

        
        WIN.fill(YELLOW) #bg color 
        pg.draw.rect(WIN, GREEN, cat) # draw the cat on screen
        # cat.x +=cat_speed
        
        
        pg.display.update()