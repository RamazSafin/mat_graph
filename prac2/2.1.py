import pygame as pg
import numpy as np
import sys

pg.init()

sc = pg.display.set_mode((1000, 1000))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

matrix = np.array([[0, 100], [200, 300]], dtype=float)
T = np.array([[1, 2], [3, 1]], dtype=float)

t_matrix = matrix @ T
mid_point = np.mean(matrix, axis=0)
mid_transformed = np.mean(t_matrix, axis=0)

pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    sc.fill(WHITE)

    pg.draw.line(sc, BLACK, (matrix[0][0], matrix[0][1]), (matrix[1][0], matrix[1][1]), 5)

    pg.draw.line(sc, BLACK, (t_matrix[0][0], t_matrix[0][1]), (t_matrix[1][0], t_matrix[1][1]), 5)

    pg.draw.circle(sc, BLACK, (mid_point[0], mid_point[1]), 5)

    pg.draw.circle(sc, BLACK, (mid_transformed[0], mid_transformed[1]), 5)

    pg.display.flip()

pg.quit()
sys.exit()
