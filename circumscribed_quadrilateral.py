from tools.geometry import *

if __name__ == '__main__':
    ax, ay, bx, by, cx, cy = map(int, input().split())
    ex, ey, fx, fy = map(int, input().split())
    A = P(ax, ay)
    B = P(bx, by)
    C = P(cx, cy)
    E = P(ex, ey)
    F = P(fx, fy)

    O = perp_bisector(A, B).intersect(perp_bisector(B, C))
    P1, P2 = line_circle_intersection(O, distance(O, A), Line.by_points(E, F))
    if E.x <= P1.x <= F.x or F.x <= P1.x <= E.x:
        D = P1
    else:
        D = P2

    S = 0.5*abs(skew(Vec(D, A), Vec(D, C))) + 0.5*abs(skew(Vec(B, A), Vec(B, C)))

    print(f"{S:.5f}")
