import math
from tools.stereopoint import *


class QVec:  # Геометрический вектор (начало + конец)
    def __init__(self, P1: Q, P2: Q):
        self.P1 = P1 if P1 is not None else Q(0, 0, 0)
        self.P2 = P2

    @property
    def x(self):
        return self.P2.x - self.P1.x

    @property
    def y(self):
        return self.P2.y - self.P1.y

    @property
    def z(self):
        return self.P2.z - self.P1.z

    @property
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __eq__(self, other):
        return self.P1 == other.P1 and self.P2 == other.P2

    def __str__(self):
        return str(self.P1) + " " + str(self.P2)


def vec_abs(V1: QVec, V2: QVec):  # Векторное произведение векторов (длина)
    return math.sqrt((V1.y*V2.z - V1.z*V2.y)**2 +
                     (V1.z*V2.x - V1.x*V2.z)**2 +
                     (V1.x*V2.y - V1.y*V2.x)**2)


def dot(V1: QVec, V2: QVec):  # Скалярное произведение векторов
    return V1.x * V2.x + V1.y * V2.y + V1.z * V2.z
