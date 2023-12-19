import pygame
import numpy as np

pygame.init()


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

def display_coordinates(screen, color, coordinates, label):
    font = pygame.font.Font(None, 36)
    text = font.render(f'{label}: ({coordinates[0]}, {coordinates[1]})', True, color)
    screen.blit(text, (coordinates[0] + 10, coordinates[1] + 10))

def main():
    x1 = float(input("Введите координату x первой точки: "))
    y1 = float(input("Введите координату y первой точки: "))
    point1 = np.array([x1, y1])

    x2 = float(input("Введите координату x второй точки: "))
    y2 = float(input("Введите координату y второй точки: "))
    point2 = np.array([x2, y2])

    line_matrix = np.vstack((point1, point2))

    transformation_matrix = np.array([[1, 3],
                                      [4, 1]])

    new_line_matrix = np.dot(line_matrix, transformation_matrix)

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Матричное преобразование линии")

    pygame.draw.line(screen, BLUE, (x1, y1), (x2, y2), 2)

    pygame.draw.line(screen, RED, (new_line_matrix[0, 0], new_line_matrix[0, 1]),
                     (new_line_matrix[1, 0], new_line_matrix[1, 1]), 2)

    display_coordinates(screen, BLUE, point1, 'Точка 1')
    display_coordinates(screen, BLUE, point2, 'Точка 2')
    display_coordinates(screen, RED, new_line_matrix[0], 'Новая точка 1')
    display_coordinates(screen, RED, new_line_matrix[1], 'Новая точка 2')

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
