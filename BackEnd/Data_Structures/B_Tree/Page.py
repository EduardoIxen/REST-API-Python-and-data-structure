from BackEnd.Obj.Course import Course


class Page:
    def __init__(self, _m):
        self.count = 0
        self.m = _m
        self.keys = [Course(0, "", 0, 0, False) for x in range(_m)]
        self.leaf = [Page for x in range(_m)]

        for i in range(_m):
            self.leaf[i] = None

    def max_keys(self):
        return self.count == self.m - 1
