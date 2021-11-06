from BackEnd.Data_Structures.Sparse_Matrix.NodeM import NodeM

class Hour(NodeM):
    def __init__(self, hour):
        NodeM.__init__(self)
        self.hour = hour

    def print_v(self):
        return 'Hour: '+ str(self.hour)

    def getValue(self):
        return self.hour

