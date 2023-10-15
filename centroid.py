from tools.geometry import *

if __name__ == '__main__':
    ax, ay, bx, by, dx, dy, ex, ey = map(int, input().split())
    A = P(ax, ay)
    B = P(bx, by)
    D = P(dx, dy)
    E = P(ex, ey)

    l = Line.by_points(B, D).parallel((Vec(B, A)*(1/3)).P2)
    G = l.intersect(Line.by_points(E, D))
    C = Line.by_points(B, D).intersect(Line.by_points(middle_point(A, B), G))

    print(f"{C.x:.5f}")
