import queue
from graphviz import Source
import os


def graphTree(root, title):
    titulo = "labelloc = \"t\";label = \"ARBOL B DE CURSOS "+title+"\";fontsize = \"22\";"
    accumulated = ["digraph G\n{\nnode[shape = record, height= .1];\n"+titulo+"\n", "", 0, 0]
    if root is not None:
        _queue = queue.Queue()
        _queue.put(root)
        while not(_queue.empty()):
            tmpPage = _queue.get()
            __print(tmpPage, accumulated)
            i = 0
            while i <= tmpPage.count:
                if tmpPage.leaf[i] is not None:
                    _queue.put(tmpPage.leaf[i])
                i += 1
            accumulated[2] += 1
        accumulated[0] += "\n" + accumulated[1]
    accumulated[0] += "}\n"

    #src = Source(accumulated[0], filename="../FrontEnd/SmartClass/src/assets/img/graphCourseStudent", format="svg")
    #src.view()
    f = open("../FrontEnd/SmartClass/src/assets/img/graphCourseStudent.dot", 'w')
    try:
        f.write(accumulated[0])
    finally:
        f.close()

    prog = "dot -Tsvg  ../FrontEnd/SmartClass/src/assets/img/graphCourseStudent.dot -o ../FrontEnd/SmartClass/src/assets/img/graphCourseStudent.svg"
    os.system(prog)


def __print(current, accumulated):
    accumulated[0] += 'node{}[label="<r0>'.format(str(accumulated[2]))

    if current.leaf[0] is not None:
        accumulated[3] += 1
        accumulated[1] += '"node{}":r0 -> "node{}"\n'.format(str(accumulated[2]), str(accumulated[3]))

    i = 1
    while i <= current.count:
        if current.keys[i].code == 13:
            pass
        accumulated[0] += '|<c{}> {} |<r{}>'.format(str(i),str(current.keys[i].code) +'\\n'+current.keys[i].name, str(i))

        if current.leaf[i] is not None:
            accumulated[3] += 1
            accumulated[1] += '"node{}":r{} -> "node{}"\n'.format(str(accumulated[2]) ,str(i), str(accumulated[3]))
        i += 1
    accumulated[0] += '"];\n'

