import math


class Q:  # Трехмерная точка
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z)


def distance(P1: Q, P2: Q):  # Расстояние м-ду 2-мя точками
    return math.sqrt((P2.x - P1.x) ** 2 + (P2.y - P1.y) ** 2 + (P2.z - P1.z) ** 2)


def middle_point(P1: Q, P2: Q, divide=True):  # Медиана отрезка
    if divide:
        return Q((P1.x + P2.x) / 2, (P1.y + P2.y) / 2, (P1.z + P2.z) / 2)
    else:
        return Q(P1.x + P2.x, P1.y + P2.y, P1.z + P2.z)  # для более точных операций
