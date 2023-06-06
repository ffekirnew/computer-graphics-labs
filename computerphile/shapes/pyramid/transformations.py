from typing import List

import numpy as np

Point = float

Vector = np.array
Vectors = List[Vector]

ScalingVector = Vector
TranslationVector = Vector

Angle = float


class Transformation:
    @staticmethod
    def scale(scalar_vector: ScalingVector, vectors: Vectors) -> Vectors:
        return [np.multiply(vector, scalar_vector) for vector in vectors]

    @staticmethod
    def translate(translation_vector: TranslationVector, vectors: Vectors) -> Vectors:
        return [np.add(vector, translation_vector) for vector in vectors]

    @staticmethod
    def rotate(angle: Angle, axis: Vector, vectors: Vectors) -> Vectors:
        pass


if __name__ == '__main__':
    vertices = [
        np.array([0, 1, 0]),  # top
        np.array([-1, -1, 1]),  # front left
        np.array([1, -1, 1]),  # front right
        np.array([1, -1, -1]),  # back right
        np.array([-1, -1, -1])  # back left
    ]
    print(Transformation.scale(np.array([1, 2, 4]), vertices))
    print(Transformation.translate(np.array([1, 2, 4]), vertices))
