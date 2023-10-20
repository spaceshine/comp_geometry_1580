from tools.geometry import *


def ellipse(P0: P, A: P, B: P, r):
    eq = distance(A, P0) + distance(B, P0) - r
    if round(eq, 6) == 0:
        return 0
    if eq > 0:
        return 1
    return -1


if __name__ == '__main__':
    ax, ay, bx, by, r = map(int, input().split())
    ex, ey, fx, fy = map(int, input().split())
    A = P(ax, ay)
    B = P(bx, by)
    E = P(ex, ey)
    F = P(fx, fy)
    # пусть точка E лежит внутри, а F - снаружи
    if ellipse(E, A, B, r) > 0:
        E, F = F, E

    M = E
    search = True
    while search:
        M = middle_point(E, F)
        side = ellipse(M, A, B, r)
        if side == 0:
            search = False
        elif side == 1:
            F = M
        else:
            E = M

    print(f"{M.x:.5f}\n{M.y:.5f}")
