from abc import ABC, abstractmethod


class Double_Linked_List(ABC):
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def search(self):
        pass

