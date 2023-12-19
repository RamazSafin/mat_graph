import numpy as np
import matplotlib.pyplot as plt

def apply_transformation(point, transformation_matrix):
    return np.dot(transformation_matrix, point)

def plot_point(ax, point, color, label):
    ax.scatter(point[0], point[1], c=color)
    ax.annotate(f'{label}: ({point[0]}, {point[1]})', (point[0], point[1]), textcoords="offset points", xytext=(5,5), ha='center', fontsize=8)

def main():
    x = float(input("Введите координату x точки: "))
    y = float(input("Введите координату y точки: "))
    point = np.array([x, y])

    matrix = np.array([[1, 3],
                       [4, 1]])

    new_point = apply_transformation(point, matrix)

    fig, ax = plt.subplots()
    plot_point(ax, point, 'blue', 'Исходная')
    plot_point(ax, new_point, 'red', 'Новая')

    print("x =", x)
    print("y =", y)

    print(matrix)

    print("x' =", new_point[0])
    print("y' =", new_point[1])

    plt.show()

if __name__ == "__main__":
    main()
