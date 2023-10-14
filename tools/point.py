import math

class P:  # Точка
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return str(self.x) + " " + str(self.y)


def distance(P1: P, P2: P):  # Расстояние м-ду 2-мя точками
    return math.sqrt((P2.x - P1.x) ** 2 + (P2.y - P1.y) ** 2)


def middle_point(P1: P, P2: P, divide=True):  # Медиана отрезка
    if divide:
        return (P1.x + P2.x) / 2, (P1.y + P2.y) / 2
    else:
        return P1.x + P2.x, P1.y + P2.y  # для более точных операций
