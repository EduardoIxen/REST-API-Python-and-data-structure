#from NodeTreeAvl import NodeTreeAvl
from Data_Structures.NodeTreeAvl import NodeTreeAvl


class ABB:
    def __init__(self):
        self.root = None
        self.height = -1
        self.balance = 0

    def insert(self, student):
        node = NodeTreeAvl(student)
        if self.root is None:
            self.root = node
            self.root.left = ABB()
            self.root.right = ABB()
        elif student.carnet > self.root.student.carnet:
            self.root.right.insert(student)
        elif student.carnet < self.root.student.carnet:
            self.root.left.insert(student)
        else:
            print(F"EL ESTUDIANTE CON CARNET {student.carnet} ya existe.")
            return
        self.balance_tree()

    def balance_tree(self):
        self.update_height(recursivity=False)
        self.update_balance(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.root.left.balance < 0:
                    self.root.left.left_rotation()
                    self.update_height()
                    self.update_balance()
                self.right_rotation()
                self.update_height()
                self.update_balance()
            if self.balance < -1:
                if self.root.right.balance > 0:
                    self.root.right.right_rotation()
                    self.update_height()
                    self.update_balance()
                self.left_rotation()
                self.update_height()
                self.update_balance()

    def update_height(self, recursivity = True):
        if self.root == None:
            self.height = -1
        else:
            if recursivity:
                if self.root.left != None:
                    self.root.left.update_height()
                if self.root.right != None:
                    self.root.right.update_height()
            self.height = max(self.root.left.height, self.root.right.height) + 1

    def update_balance(self, recursivity = True):
        if self.root is None:
            self.balance = 0
        else:
            if recursivity:
                if self.root.left != None:
                    self.root.left.update_balance()
                if self.root.right != None:
                    self.root.right.update_balance()
            self.balance = self.root.left.height - self.root.right.height

    def right_rotation(self):
        root = self.root
        self.root = root.left.root
        root.left.root = self.root.right.root
        self.root.right.root = root

    def left_rotation(self):
        root = self.root
        self.root = root.right.root
        root.right.root = self.root.left.root
        self.root.left.root = root

    def delete_student(self, carnet):
        self.root = self.delete_student2(self.root, carnet)
        #self.balance_tree()

    def delete_student2(self, root, carnet):
        if root is None:
            return root

        if carnet < root.student.carnet:
            root.left.root = self.delete_student2(root.left.root, carnet)
            return root
        elif carnet > root.student.carnet:
            root.right.root = self.delete_student2(root.right.root, carnet)
            return root

            # Para un nodo hoja
        if root.left.root is None and root.right.root is None:
            if self.root == root:
                self.root = None
            return None

            # para un nodo con un solo hijo
        if root.left.root is None:
            temp = root.right.root
            root = None
            return temp

        if root.right.root is None:
            temp = root.left.root
            root = None
            return temp

            # Para un nodo con dos hijos
        tempPadre = root

        succ = root.right.root
        while succ.left.root != None:
            tempPadre = succ
            succ = succ.left.root

        if tempPadre != root:
            tempPadre.left.root = succ.right.root
        else:
            tempPadre.right.root = succ.right.root

        root.student = succ.student

        return root

    '''
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
    '''
    def search(self, key):
        return self.search2(self.root, key)

    def search2(self, local_root, key):
        if local_root is None or local_root.student.carnet == key:
            return local_root
        if local_root.student.carnet < key:
            return self.search2(local_root.right.root, key)
        return self.search2(local_root.left.root, key)

    def search_login(self, root, key, password):
        if root is None:
            return False
        elif root.student.carnet == key and root.student.password == password:
            return True
        elif root.student.carnet > key:
            value = self.search_login(root.left.root, key, password)
            return value
        else:
            value = self.search_login(root.right.root, key, password)
            return value
