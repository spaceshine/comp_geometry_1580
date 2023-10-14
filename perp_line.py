import math
from tools.geometry import *


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    x0, y0 = map(int, input().split())

    print(Line(a, b, c).perpendicular(P(x0, y0)))
