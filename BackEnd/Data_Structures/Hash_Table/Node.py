class Node:
    def __init__(self, key, carnet, title, content):
        self.key = key
        self.carnet = carnet
        self.title = title
        self.content = content
        self.next = None