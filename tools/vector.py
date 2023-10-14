import math
from tools.point import *

class Vec:  # Геометрический вектор (начало + конец)
    def __init__(self, P1: P, P2: P):
        self.P1 = P1 if P1 is not None else (0, 0)
        self.P2 = P2

    @property
    def x(self):
        return self.P2.x - self.P1.x

    @property
    def y(self):
        return self.P2.y - self.P1.y

    def to_avec(self):
        return AVec(self.x, self.y)

    def norm(self):
        norm_avec = self.to_avec().norm()
        return Vec(self.P1, P(self.P1.x + norm_avec.x, self.P1.y + norm_avec.y))

    def __eq__(self, other):
        return self.P1 == other.P1 and self.P2 == other.P2

    def __mul__(self, other: float):
        mul_avec = self.to_avec()*other
        return Vec(self.P1, P(self.P1.x + mul_avec.x, self.P1.y + mul_avec.y))

    def __add__(self, other):
        return Vec(self.P1, P(self.P2.x + other.x, self.P2.y + other.y))

    def __str__(self):
        return str(self.P1) + " " + str(self.P2)


class AVec:  # Алгебраический вектор (только координаты)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_vec(self, P_start):
        return Vec(P_start, P(P_start.x + self.x, P_start.y + self.y))

    def norm(self):
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        return AVec(self.x / length, self.y / length)

    def perpendiculars(self):
        return AVec(-self.y, self.x), AVec(self.y, -self.x)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return AVec(self.x + other.x, self.y + other.y)

    def __mul__(self, other: float):
        return AVec(self.x * other, self.y * other)

    def __str__(self):
        return str(self.x) + " " + str(self.y)


def skew(V1: Vec or AVec, V2: Vec or AVec):  # Косое произведение векторов
    return V1.x * V2.y - V2.x * V1.y


def dot(V1: Vec or AVec, V2: Vec or AVec):  # Скалярное произведение векторов
    return V1.x * V2.x + V1.y * V2.y