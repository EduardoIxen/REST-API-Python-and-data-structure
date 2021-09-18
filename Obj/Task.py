from Data_Structures.Sparse_Matrix.NodeM import NodeM


class Task(NodeM):
    def __init__(self, _carnet, _name, _description, _course, _date, _hour, _status):
        NodeM.__init__(self)
        self.carnet = _carnet
        self.name = _name
        self.description = _description
        self.course = _course
        self.date = _date
        self.hour = _hour
        self.status = _status

    def print_v(self):
        pass

    def getValue(self):
        return self.carnet


