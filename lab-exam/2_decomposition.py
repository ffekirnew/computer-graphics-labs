# Write a python function named decompose_matrices that can an array as a parameter and returns 3 decomposed matrices using singular value decomposition technique.
import numpy as np

def decompose_matrices(array):
    return np.linalg.svd(array)

def test():
    array = np.array([
        [3,4,3],
        [1,2,3],
        [4,2,1]
    ])

    print(decompose_matrices(array))

if __name__ == "__main__":
    test()