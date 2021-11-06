from abc import ABC, abstractmethod


class NodeM(ABC):
    def __init__(self):
        self.left = None
        self.right = None
        self.up = None
        self.down = None

        self.next = None
        self.previous = None

    @abstractmethod
    def print_v(self):
        pass

    @abstractmethod
    def getValue(self):
        pass
