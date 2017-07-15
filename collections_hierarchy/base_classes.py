from .node import Node


class Sequenceable(object):
    def __init__(self):
        #define start and end nodes
        self.start=None
        self.end=None

    def get_elements(self):
        current=self.start
        list1 = []
        if self.start == None:
            print(list1)
        while current is not None:
            list1 += current.value
            current = current.next
        return list1
        
class Appendable(object):
    def append(self, element):
        element1= Node(element)
        if self.start == None:
            self.start = element1
        if self.end != None:
            self.end.next=element1
        self.end=element1

class Popable(object):
    def pop(self):
        if self.start == None:
            raise IndexError()
        current = self.start 
        self.start = current.next
        return current.value


class Pushable(object):
    def push(self, element):
        element1 = Node(element)
        if self.start == None:
            self.start = element1
        #current = self.start.value
        else:
            element1.next = self.start
            self.start = element1       
