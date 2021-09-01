from graphviz import Digraph


class ABB_Graph:
    def __init__(self):
        pass

    def graph_avl(self, root):
        dot = Digraph(filename="ArbolAVL", format="svg")
        dot.attr('node', shape='circle')
        self.through_avl(root, dot)
        dot.render("./Report/ArbolAVL", view=True)


    def through_avl(self, root, dot):
        if root:
            dot.node(str(hash(root)), str(root.student.carnet))
            if root.left.root != None:
                dot.edge(str(hash(root)), str(hash(root.left.root)))
            if root.right.root != None:
                dot.edge(str(hash(root)), str(hash(root.right.root)))
            self.through_avl(root.left.root, dot)
            self.through_avl(root.right.root, dot)
