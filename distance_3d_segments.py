from tools.stereovector import *


def distance_to_segment(O: Q, A: Q, B: Q):
    if dot(QVec(A, B), QVec(A, O)) <= 0:
        return distance(A, O)
    if dot(QVec(B, A), QVec(B, O)) <= 0:
        return distance(B, O)
    return abs(vec_abs(QVec(A, B), QVec(A, O)))/distance(A, B)


if __name__ == '__main__':
    ax, ay, az, bx, by, bz = map(int, input().split())
    cx, cy, cz, dx, dy, dz = map(int, input().split())
    A = Q(ax, ay, az)
    B = Q(bx, by, bz)
    C = Q(cx, cy, cz)
    D = Q(dx, dy, dz)

    M = A
    dA = distance_to_segment(A, C, D)
    dB = distance_to_segment(B, C, D)
    dM = dA
    search = True
    while search:
        M = middle_point(A, B)
        dM = distance_to_segment(M, C, D)

        # print(M, A, B)
        # print(dM, dA, dB)
        if round(dA - dM, 7) == 0 or round(dB - dM, 7) == 0:
            search = False
            # print("# 1")
        elif dM >= dB and dM >= dA:
            search = False
            dM = min(dA, dB)
            # print("# 2")
        elif dM < dB and dB > dA:
            B = M
            dB = distance_to_segment(B, C, D)
            # print("# 3")
        elif dM < dA:
            A = M
            dA = distance_to_segment(A, C, D)
            # print("# 4")

    print(f"{dM:.6f}")
