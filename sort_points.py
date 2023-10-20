import math


class P:  # Точка
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.length = math.sqrt(x**2 + y**2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return str(self.x) + " " + str(self.y)


if __name__ == '__main__':
    n = int(input())

    P_list = []
    for _ in range(n):
        px, py = map(int, input().split())
        P_list.append(P(px, py))

    print(*sorted(P_list, key=lambda x: x.length), sep='\n')
