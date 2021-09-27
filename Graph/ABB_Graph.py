from graphviz import Digraph


class ABB_Graph:
    def __init__(self):
        pass

    def graph_avl(self, root):
        dot = Digraph(filename="ArbolAVL", format="svg")
        dot.attr('node', shape='circle')
        dot.graph_attr["labelloc"] = "t"
        dot.graph_attr["label"] = "ARBOL AVL DE ESTUDIANTES"
        dot.graph_attr["fontsize"] = "22"
        self.through_avl(root, dot)
        dot.render("./Report/ArbolAVL", view=True)


    def through_avl(self, root, dot):
        if root:
            #content = str(root.student.carnet) + "\n" + root.student.name + "\n" + root.student.degree[0:20] + "\n" + root.student.degree[20:40]
            content = str(root.student.carnet) + "\n" + root.student.name[0:12]
            dot.node(str(hash(root)), content)
            if root.left.root != None:
                dot.edge(str(hash(root)), str(hash(root.left.root)))
            if root.right.root != None:
                dot.edge(str(hash(root)), str(hash(root.right.root)))
            self.through_avl(root.left.root, dot)
            self.through_avl(root.right.root, dot)
