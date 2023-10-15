from tools.geometry import *

if __name__ == '__main__':
    ax, ay, bx, by, dx, dy, ex, ey = map(int, input().split())
    A = P(ax, ay)
    B = P(bx, by)
    D = P(dx, dy)
    E = P(ex, ey)

    I = bisect_line(A, B, D if D.x < B.x else (Vec(B, D)*(-1)).P2).intersect(Line.by_points(E, D))
    B_ = reflect(B, Line.by_points(A, I))
    C = Line.by_points(A, B_).intersect(Line.by_points(B, D))

    print(f"{C.x:.5f}")
