from tools.point import *
from tools.vector import *
from tools.line import *


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


def perp_bisector(A: P, B: P):
    return Line.by_normal(middle_point(A, B), Vec(A, B))


def equilateral_triangle(P1: P, P2: P):  # равносторонний треугольник на [P1 P2]
    main_side = Vec(P1, P2)
    perp_bisectors = main_side.to_avec().perpendiculars()

    return [(main_side*0.5 + perp*(math.sqrt(3)/2)).P2 for perp in perp_bisectors]


def is_segment_intersection(V1: Vec, V2: Vec):  # проверяет пересекаются ли отрезки [A B] и [C D]
    A, B = V1.P1, V1.P2
    C, D = V2.P1, V2.P2
    sk1 = skew(Vec(A, B), Vec(A, C)) * skew(Vec(A, B), Vec(A, D))
    sk2 = skew(Vec(C, D), Vec(C, A)) * skew(Vec(C, D), Vec(C, B))

    if sk1 == 0 and sk2 == 0:
        if dot(Vec(C, A), Vec(C, B)) <= 0 or \
                dot(Vec(D, A), Vec(D, B)) <= 0 or \
                dot(Vec(A, C), Vec(A, D)) <= 0 or \
                dot(Vec(B, C), Vec(B, D)) <= 0:
            return True
        else:
            return False

    if sk1 <= 0 and sk2 <= 0:
        return True
    return False
