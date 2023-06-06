import numpy as np


def show_determinant(array):
    return np.linalg.det(array)


def test():
    array = np.array([
        [1, 2],
        [3, 4]
    ])

    print(show_determinant(array))


if __name__ == "__main__":
    test()
