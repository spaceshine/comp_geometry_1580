from tools.geometry import *


if __name__ == '__main__':
    ax, ay, bx, by = map(float, input().split())
    V0 = Vec(P(ax, ay), P(bx, by))

    n = int(input())
    lst = []
    for i in range(1, n+1):
        ax, ay, bx, by = map(float, input().split())
        Vi = Vec(P(ax, ay), P(bx, by))
        if is_segment_intersection(V0, Vi):
            lst.append(i)

    print(len(lst))
    print(*lst)
