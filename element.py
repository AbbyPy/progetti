class Point:
    """ class for creating point obj """
    def __init__(self, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
        except:
            raise ValueError("x, y must be float")


class Line:
    """ class for creating line obj """
    def __init__(self, m, q):
        try:
            self.m = float(m)
            self.q =float(q)
        except:
            raise ValueError("m, q must be float")
