from graphviz import Digraph


class List_Graph:
    def __init__(self):
        pass
    def graph_list(self, first):
        dot = Digraph(filename="list_task",format="svg")
        dot.graph_attr["rankdir"] = "LR"
        dot.attr('node', shape='rectangle')
        self.through_list(first, dot)
        dot.render("./Report/list_task", view=True)

    def through_list(self, first, dot):
        temp = first
        while temp is not None:
            content = temp.carnet + "\n" + temp.name
            dot.node(str(hash(temp)), content)
            if temp.next is not None:
                dot.edge(str(hash(temp)), str(hash(temp.next)), dir="both")
            temp = temp.next
