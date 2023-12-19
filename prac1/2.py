import pygame as pg
import sys

pg.init()

sc = pg.display.set_mode((600, 600))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKCYAN = (0, 139, 139)

pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    sc.fill(WHITE)

    pg.draw.circle(sc, BLACK, (300, 200), 50)

    pg.draw.rect(sc, DARKCYAN, (150, 150, 100, 100))

    pg.display.flip()

pg.quit()
sys.exit()