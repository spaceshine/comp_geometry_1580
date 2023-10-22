import math
from tools.point import *
from tools.vector import *


class Line:  # прямая на плоскости (ax + by + c = 0)
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def by_points(P1: P, P2: P):
        a = P1.y - P2.y
        b = P2.x - P1.x
        c = P1.x * (P2.y - P1.y) - P1.y * (P2.x - P1.x)
        return Line(a, b, c)

    @staticmethod
    def by_normal(P0: P, N: Vec or AVec):
        return Line(N.x, N.y, -1 * (N.x * P0.x + N.y * P0.y))

    @staticmethod
    def by_vector(P0: P, V: Vec or AVec):
        return Line(V.y, -V.x, V.x * P0.y - V.y * P0.x)

    def intersect(self, other):
        x = -1 * skew(AVec(self.c, other.c), AVec(self.b, other.b)) / skew(AVec(self.a, other.a), AVec(self.b, other.b))
        y = skew(AVec(self.c, other.c), AVec(self.a, other.a)) / skew(AVec(self.a, other.a), AVec(self.b, other.b))
        return P(x, y)

    def distance(self, P0: P):
        return abs((self.a * P0.x + self.b * P0.y + self.c) / math.sqrt(self.a ** 2 + self.b ** 2))

    def perpendicular(self, P0: P):
        return Line(-self.b, self.a, self.c + self.b*(P0.x + P0.y) + self.a*(P0.x - P0.y))

    def parallel(self, P0: P):
        return Line(self.a, self.b, -(self.a * P0.x + self.b * P0.y))

    def __str__(self):
        return f"{self.a} {self.b} {self.c}"


def reflect(P0: P, l: Line):  # отражение точки относительно прямой
    # решение системы линейных уравнений (middle_point(P0, P_) -> l) and (Vec(P0, P_) is_perp l)
    x_ = -(2*l.a*l.b*P0.y + (l.a**2 - l.b**2)*P0.x + 2*l.a*l.c) / (l.a**2 + l.b**2)
    y_ = -(2*l.a*l.b*P0.x + (l.b**2 - l.a**2)*P0.y + 2*l.b*l.c) / (l.a**2 + l.b**2)

    return P(x_, y_)
