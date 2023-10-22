from tools.geometry import *


class Mirror:
    def __init__(self, P1: P, P2: P):
        self.P1 = P1
        self.P2 = P2

    def reflect_p(self, X: P):
        # необходимо проверить с какой стороны зеркала расположена точка
        if skew(Vec(self.P1, X), Vec(self.P1, self.P2)):
            return reflect(X, Line.by_vector(self.P1, Vec(self.P1, self.P2)))

    def reflect(self, other):
        P1_ = self.reflect_p(other.P1)
        P2_ = self.reflect_p(other.P2)
        return Mirror(P2_, P1_)


if __name__ == '__main__':
    pass
