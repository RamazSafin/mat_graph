import numpy as np

def mainc():
    x = float(input("Введите координату x точки: "))
    y = float(input("Введите координату y точки: "))
    point = np.array([x, y])
    matrix = np.array([[1, 3],
                       [4, 1]])
    new_point = np.dot(matrix, point)

    print("x =", x)
    print("y =", y)

    print(matrix)

    print("x' =", new_point[0])
    print("y' =", new_point[1])

if __name__ == "__main__":
    mainc()
