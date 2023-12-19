import numpy as np
import pygame
import sys

WHITE = (255, 255, 255)
PURPLE = (240, 130, 230)

L = np.array([[8, 1], [7, 3], [6, 2]])
L = L*100

T = np.array([[0, 1], [1, 0]])

L_conv = L @ T

pygame.init()

screen = pygame.display.set_mode((1300, 850))
screen.fill(WHITE)

pygame.draw.polygon(screen, PURPLE, [(L[0, 0], L[0, 1]), (L[1, 0], L[1, 1]), (L[2, 0], L[2, 1])], 5)

pygame.draw.line(screen, PURPLE, (0, 0), (850, 850), 3)

pygame.draw.polygon(screen, PURPLE, [(L_conv[0, 0], L_conv[0, 1]), (L_conv[1, 0], L_conv[1, 1]), (L_conv[2, 0], L_conv[2, 1])], 5)

FPS = 30
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(FPS)
    pygame.display.update()