import os
from BackEnd.Data_Structures.Sparse_Matrix.Matrix import Matrix
from graphviz import Source


class Matrix_Graph:
    def __init__(self):
        pass
    def graph_matrix(self, matriz):
        acumInfo = """digraph G{
        node[shape=box, width = 1.5, style=filled, color=SpringGreen3];
        edge[color=black];
        rankdir=UD;
        Matriz[label="Matriz", width = 1.5, style = filled, fillcolor = MediumOrchid1, gropu = fila];
        labelloc="t";
        label = "DIAS";
        fontsize="22";\n"""

        idCabeceraFila = ""
        cabeceraFila = ""

        idCabeceraCol = ""
        cabeceraCol = ""

        alineacionCol = "{rank=same; Matriz;"
        alineacionElementosFila = ""
        alineacionElementosColumna = ""

        cabeceraElementosFila = ""
        enlacesElementosFila = ""

        cabeceraElementosColumna = ""
        enlacesElementosColumna = ""

        # RECORRIDO DE FILAS
        eFila = matriz.head_row.first
        if eFila != None:
            cabeceraFila += 'Matriz -> "{}";\n'.format(str(hash(eFila)))
            # RECORRER TODAS LAS FILAS DE LA MATRIZ

            while eFila != None:
                # elemntos fila
                alineacionElementosFila += '{{rank=same; {};'.format(str(hash(eFila)))
                infoFilas = self.recorrerFilasMatriz(eFila)
                alineacionElementosFila += infoFilas[0] + "}\n"
                cabeceraElementosFila += infoFilas[1] + "\n"
                enlacesElementosFila += infoFilas[2] + "\n"

                idCabeceraFila += '"{}"[label = "{}",width = 1.5, group=fila, style=filled, color=DarkOrange1];\n'.format(
                    str(hash(eFila)), str(eFila.getValue())+":00")
                if eFila.next != None:
                    # filas
                    cabeceraFila += '"{}" -> "{}" [dir="both"];\n'.format(str(hash(eFila)), str(hash(eFila.next)))
                eFila = eFila.next


        # RECORRIDO DE COLUMNAS
        eCol = matriz.head_column.first
        if eCol != None:
            cabeceraCol += 'Matriz -> "{}";\n'.format(str(hash(eCol)))
            while eCol != None:
                infoCols = self.recorrerColumnasMatriz(eCol)
                enlacesElementosColumna += infoCols[2] + "\n"

                # COLUMNAS
                alineacionCol += '"{}";'.format(str(hash(eCol)))
                idCabeceraCol += '"{}"[label="{}", group={},width = 1.3, style=filled, color=RoyalBlue1];\n'.format(
                    str(hash(eCol)), str(eCol.getValue()), str(eCol.getValue()))
                if eCol.next != None:
                    cabeceraCol += '"{}" -> "{}" [dir="both"];\n'.format(str(hash(eCol)), str(hash(eCol.next)))
                else:
                    alineacionCol += '}\n\n'
                eCol = eCol.next


        acumInfo += alineacionCol + alineacionElementosFila + alineacionElementosColumna \
                    + idCabeceraCol + idCabeceraFila + cabeceraElementosFila + \
                    cabeceraElementosColumna + cabeceraCol + \
                    cabeceraFila + enlacesElementosFila + \
                    enlacesElementosColumna + "\n}\n"

        s = Source(acumInfo, filename="./Report/matrix", format="svg")
        s.view()


    def recorrerFilasMatriz(self, nodoFila):
        rank = ""
        enlaces = ""
        cabeceras = ""
        tmp = nodoFila.right
        enlaces += '"{}" -> "{}";\n'.format(str(hash(nodoFila)), str(hash(tmp)))
        while tmp != None:
            rank += '"{}";'.format(str(hash(tmp)))
            cabeceras += '"{}"[label = "{}", group={}];\n'.format(str(hash(tmp)), str(tmp.getValue()), str(tmp.column))
            if tmp.right != None:
                enlaces += '"{}" -> "{}" [dir="both"];\n'.format(str(hash(tmp)), str(hash(tmp.right)))
            tmp = tmp.right
        # cabeceras += '"{}"[label = "{}"];\n'.format(str(hash(tmp)), str(tmp.getValue()))
        return [rank, cabeceras, enlaces]

    def recorrerColumnasMatriz(self, nodoCol):
        rank = ""
        enlaces = ""
        cabeceras = ""
        tmp = nodoCol.down
        enlaces += '"{}" -> "{}";\n'.format(str(hash(nodoCol)), str(hash(tmp)))
        while tmp != None:
            rank += '"{}";'.format(str(hash(tmp)))
            cabeceras += '"{}"[label = "{}", group={}];\n'.format(str(hash(tmp)), str(tmp.getValue()), str(tmp.column))
            if tmp.down != None:
                enlaces += '"{}" -> "{}" [dir="both"];\n'.format(str(hash(tmp)), str(hash(tmp.down)))
            tmp = tmp.down
        # cabeceras += '"{}"[label = "{}"];\n'.format(str(hash(tmp)), str(tmp.getValue()))
        return [rank, cabeceras, enlaces]
