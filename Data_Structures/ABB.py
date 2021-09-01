#from NodeTreeAvl import NodeTreeAvl
from Data_Structures.NodeTreeAvl import NodeTreeAvl


class ABB:
    def __init__(self):
        self.root = None

    def insertar(self, student):
        node = NodeTreeAvl(student)
        if self.root is None:
            self.root = node
            self.root.left = ABB()
            self.root.right = ABB()
        elif student.carnet > self.root.student.carnet:
            self.root.right.insertar(student)
        elif student.carnet < self.root.student.carnet:
            self.root.left.insertar(student)
        else:
            print(F"EL ESTUDIANTE CON CARNET {student.carnet} ya existe.")

    def buildTree(self, root):
        nodes = []
        self.storeBSTNodes(self.root, nodes)

        n = len(nodes)
        self.root = self.buildTreeUtil(nodes, 0, n-1)

    def storeBSTNodes(self, root, nodes):
        if root is None:
            return
        self.storeBSTNodes(root.left.root, nodes)
        nodes.append(root)
        self.storeBSTNodes(root.right.root, nodes)

    def buildTreeUtil(self,nodes, start, end):
        if start > end:
            return None

        mid = (start+end)//2
        node = nodes[mid]
        node.left.root = self.buildTreeUtil(nodes, start, mid-1)
        node.right.root = self.buildTreeUtil(nodes, mid+1, end)
        return node
