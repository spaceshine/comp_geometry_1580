from tools.geometry import *

if __name__ == '__main__':
    ax, ay, bx, by, dx, dy, ex, ey = map(int, input().split())
    A = P(ax, ay)
    B = P(bx, by)
    D = P(dx, dy)
    E = P(ex, ey)

    p1 = Line.by_normal(A, Vec(B, D))
    H = Line.by_points(E, D).intersect(p1)
    p2 = Line.by_normal(H, Vec(A, B))
    C = Line.by_points(B, D).intersect(p2)

    print(f"{C.x:.5f}")
