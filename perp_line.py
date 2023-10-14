import math


class P:  # Точка
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return str(self.x) + " " + str(self.y)


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

    def __str__(self):
        return f"{self.a} {self.b} {self.c}"


def skew(V1: Vec or AVec, V2: Vec or AVec):  # Косое произведение векторов
    return V1.x * V2.y - V2.x * V1.y


def dot(V1: Vec or AVec, V2: Vec or AVec):  # Скалярное произведение векторов
    return V1.x * V2.x + V1.y * V2.y


def distance(P1: P, P2: P):  # Расстояние м-ду 2-мя точками
    return math.sqrt((P2.x - P1.x) ** 2 + (P2.y - P1.y) ** 2)


def middle_point(P1: P, P2: P, divide=True):  # Медиана отрезка
    if divide:
        return (P1.x + P2.x) / 2, (P1.y + P2.y) / 2
    else:
        return P1.x + P2.x, P1.y + P2.y  # для более точных операций


def polar_angle(A: P):
    dt = dot(AVec(1, 0), AVec(A.x, A.y))  # AVec(1, 0) - направляющий вектор Ox
    sk = skew(AVec(1, 0), AVec(A.x, A.y))
    if A.x == 0:
        return math.pi / 2 if sk > 0 else 3 * math.pi / 2

    q = math.atan(A.y / A.x)

    if sk >= 0 and dt > 0:  # 1-я четверть
        return q
    if dt < 0:  # 2-я и 3-я четверть
        return math.pi + q
    if sk < 0 and dt > 0:  # 4-я четверть
        return 2 * math.pi + q


def bisect_line(A: P, O: P, B: P):
    if skew(Vec(O, A), Vec(O, B)) == 0:
        return Line.by_normal(O, Vec(O, A))

    bisect_vec = (Vec(O, A).to_avec().norm() + Vec(O, B).to_avec().norm())
    return Line.by_vector(O, bisect_vec)


def tangent_points(O: P, r, A: P):
    d = distance(O, A)
    if d < r:
        return ()

    Vh = Vec(O, A)*((r**2) / (d**2))
    V1, V2 = (Vh.to_avec() * (math.sqrt(d**2 - r**2) / r)).perpendiculars()

    if d == r:
        return (Vh+V1).P2,

    return (Vh+V1).P2, (Vh+V2).P2


def line_circle_intersection(O: P, r, line: Line):
    h = line.distance(O)
    if h > r:
        return ()

    Vh = AVec(line.a, line.b)  # случайно выбираем направление вектора нормали
    if line.b != 0:
        X0 = P(0, -line.c/line.b)  # случайная точка на прямой
    else:
        X0 = P(-line.c/line.a, 0)
    if dot(Vh, Vec(O, X0)) < 0:  # если нормаль не по ту сторону
        Vh.x = -line.a
        Vh.y = -line.b
    Ph = (Vh.norm()*h).to_vec(O).P2

    #  откладываем от нужной точки нужные вектора в обе стороны
    V1, V2 = [(v.norm()*math.sqrt(r**2 - h**2)).to_vec(Ph) for v in Vh.perpendiculars()]
    if h == r:
        return V1.P2,
    return V1.P2, V2.P2


def circle_circle_intersection(O1: P, O2: P, r1, r2):
    if O1 == O2 and r1 == r2:
        return None, None, None

    d = distance(O1, O2)
    if d > r1 + r2 or d < abs(r1 - r2):
        return ()

    l = (r1**2 + d**2 - r2**2) / (2 * d)
    Vh = Vec(O1, O2).norm() * l
    V1, V2 = (Vec(O1, O2).to_avec().norm() * math.sqrt(r1**2 - l**2)).perpendiculars()

    if d == r1 + r2 or d == abs(r1 - r2):
        return (Vh + V1).P2,

    return (Vh + V1).P2, (Vh + V2).P2


def arc_length(O: P, r, A: P, B: P):
    if O == A or O == B:
        return 0
    cosalpha = dot(Vec(O, A), Vec(O, B)) / (distance(O, A) * distance(O, B))
    return r * math.acos(cosalpha)


def equilateral_triangle(P1: P, P2: P):  # равносторонний треугольник на [P1 P2]
    main_side = Vec(P1, P2)
    perp_bisectors = main_side.to_avec().perpendiculars()

    return [(main_side*0.5 + perp*(math.sqrt(3)/2)).P2 for perp in perp_bisectors]


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    x0, y0 = map(int, input().split())

    print(Line(a, b, c).perpendicular(P(x0, y0)))
