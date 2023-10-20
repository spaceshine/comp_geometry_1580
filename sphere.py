from tools.stereopoint import *


def sphere(P0: Q, O: Q, r):
    eq = distance(O, P0) - r
    if round(eq, 6) == 0:
        return 0
    if eq > 0:
        return 1
    return -1


if __name__ == '__main__':
    r, ox, oy, oz = map(int, input().split())
    ax, ay, az, bx, by, bz = map(int, input().split())
    O = Q(ox, oy, oz)
    A = Q(ax, ay, az)
    B = Q(bx, by, bz)
    # пусть точка A лежит внутри, а B - снаружи
    if sphere(A, O, r) > 0:
        A, B = B, A

    M = A
    search = True
    while search:
        M = middle_point(A, B)
        side = sphere(M, O, r)
        if side == 0:
            search = False
        elif side == 1:
            B = M
        else:
            A = M

    print(f"{M.x:.5f}\n{M.y:.5f}\n{M.z:.5f}")
