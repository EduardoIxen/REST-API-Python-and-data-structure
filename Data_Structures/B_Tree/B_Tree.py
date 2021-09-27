from Data_Structures.B_Tree.Page import Page
import copy


class B_Tree:
    def __init__(self, _order):
        self.order = _order
        self.root = Page(5)

    def insert(self, value):
        # [SUBE_ARRIBA, MEDIANA, ND, P]
        value_array = [False, 0, None, None]
        self.push(self.root, value, value_array)
        if value_array[0]:
            value_array[3] = Page(self.order)
            value_array[3].count = 1
            value_array[3].keys[1] = value_array[1]
            value_array[3].leaf[0] = self.root
            value_array[3].leaf[1] = value_array[2]
            self.root = value_array[3]

    # flag_page = [bool sube_arriba, int mediana, pagina nuevo,P)
    def push(self, actual_page, value, flag_page):
        way = [0]  # a que rama irse
        if actual_page is None:
            flag_page[0] = True  # sube
            flag_page[1] = value  # mediana
            flag_page[2] = None  # nueva pagina
        else:
            exist = self.search_page(actual_page, value, way)
            if exist:
                flag_page[0] = False
                return
            self.push(actual_page.leaf[way[0]], value, flag_page)
            if flag_page[0]:
                if actual_page.max_keys():
                    #self.split_node(actual_page, flag_page[1], copy.deepcopy(flag_page[2]), way, flag_page)
                    self.split_node(actual_page, flag_page[1], flag_page[2], way, flag_page)
                else:
                    flag_page[0] = False
                    self.push_leaf(actual_page, flag_page[1], flag_page[2], way[0])


    def search_page(self, actual_page, value, way):
        # Tomar en cuenta que "camino" es la direccion de las ramas por las que puede bajar la busqueda
        found = False
        if value.code < actual_page.keys[1].code: #verificar por codigo
            way[0] = 0  # Indica que vajaremos por la rama 0
            found = False
        else:  # Examina las claves del nodo en orden descendente
            way[0] = actual_page.count  #iniciamos desde la clave actual
            # Busacamos una posicion hasta donde el valor deje de ser menor
            # (por si viene un valor a los que hay en le nodo )
            while (value.code < actual_page.keys[way[0]].code) and (way[0] > 1):
                way[0] = way[0] - 1
            found = value.code == actual_page.keys[way[0]].code
        return found

    def push_leaf(self, current, value, rd, k):
        # DESPLAZAR A LA DERECHA LOS ELEMENTOS PARA HACER UN HUECO
        i = current.count
        while i >= k + 1:
            current.keys[i + 1] = current.keys[i]
            current.leaf[i + 1] = current.leaf[i]
            i = i - 1
        current.keys[k + 1] = value
        current.leaf[k + 1] = rd
        current.count = current.count + 1

    def split_node(self, actual_page, value, rd, way, flag_page):
        posMdna = self.order / 2 if (way[0] <= self.order / 2) else self.order / 2 + 1
        posMdna = int(posMdna)
        flag_page[2] = Page(5)
        i = posMdna + 1
        while i < self.order:
            # Es desplazada  la mitad drecha al nuevo nodo, la clave mediana se queda en el nodo origen
            flag_page[2].keys[i - posMdna] = actual_page.keys[i]
            flag_page[2].leaf[i - 1] = actual_page.leaf[i]
            i = i + 1
        flag_page[2].count = (self.order - 1) - posMdna  #numero de claves en le nuevo nodo
        actual_page.count = posMdna  # numero de claves en el nodo origen

        # Es insertada la clave y rama en el nodo que le corresponde
        if way[0] <= self.order / 2:   # si el camino[0 es menor al minimo de claves que puede haber en la pagina
            self.push_leaf(actual_page, value, rd, way[0])   # se inserta el nuevo alvor que trajimos en el nodo nuevo
        else:
            self.push_leaf(flag_page[2], value, rd, way[0] - posMdna)

        # se extrae la clave media del nodo origen
        flag_page[1] = actual_page.keys[actual_page.count]

        # rama 0 del nuevo nodo es la rama de la mediana
        flag_page[2].leaf[0] = actual_page.leaf[actual_page.count]
        actual_page.count = actual_page.count - 1
