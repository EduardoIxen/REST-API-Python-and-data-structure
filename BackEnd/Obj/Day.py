from BackEnd.Data_Structures.Sparse_Matrix.NodeM import NodeM


class Day(NodeM):
    def __init__(self, num):
        NodeM.__init__(self)
        self.day = num

    def print_v(self):
        return self.day

    def getValue(self):
        return self.day
