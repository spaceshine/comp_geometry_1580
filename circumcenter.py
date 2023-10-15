from tools.geometry import *

if __name__ == '__main__':
    ax, ay, bx, by, dx, dy, ex, ey = map(int, input().split())
    A = P(ax, ay)
    B = P(bx, by)
    D = P(dx, dy)
    E = P(ex, ey)

    p1 = Line.by_normal(middle_point(A, B), Vec(A, B))
    O = Line.by_points(D, E).intersect(p1)
    p2 = Line.by_normal(O, Vec(B, D))
    M = Line.by_points(B, D).intersect(p2)
    C = (Vec(B, M)*2).P2

    print(f"{C.x:.5f}")
