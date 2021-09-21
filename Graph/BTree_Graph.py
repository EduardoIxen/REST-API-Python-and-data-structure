import queue
from graphviz import Source


def graphTree(root):
    accumulated = ["digraph G\n{\nnode[shape = record, height= .1];\n", "", 0, 0]
    if root is not None:
        _queue = queue.Queue()
        _queue.put(root)
        while not(_queue.empty()):
            tmpPage = _queue.get()
            __print(tmpPage, accumulated)
            i = 0
            while i <= tmpPage.count:
                if tmpPage.leaf[i] is not None:
                    _queue.put(tmpPage.leaf[i]) #revisar el 13 y 14 no pasan
                i += 1
            accumulated[2] += 1
        accumulated[0] += "\n" + accumulated[1]
    accumulated[0] += "}\n"

    src = Source(accumulated[0], filename="./Report/B_tree", format="svg")
    src.view()


def __print(current, accumulated):
    accumulated[0] += 'node{}[label="<r0>'.format(str(accumulated[2]))

    if current.leaf[0] is not None:
        accumulated[3] += 1
        accumulated[1] += '"node{}":r0 -> "node{}"\n'.format(str(accumulated[2]), str(accumulated[3]))

    i = 1
    while i <= current.count:
        if current.keys[i].code == 13:
            print("sdp")
        accumulated[0] += '|<c{}> {} |<r{}>'.format(str(i),str(current.keys[i].code) +'\\n'+current.keys[i].name, str(i))

        if current.leaf[i] is not None:
            accumulated[3] += 1
            accumulated[1] += '"node{}":r{} -> "node{}"\n'.format(str(accumulated[2]) ,str(i), str(accumulated[3]))
        i += 1
    accumulated[0] += '"];\n';
