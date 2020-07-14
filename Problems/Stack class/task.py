class Stack:

    def __init__(self):
        self.elements = []

    def push(self, el):
        self.elements.append(el)

    def pop(self):
        remove = self.elements[-1]
        self.elements = self.elements[:-1]
        return remove

    def peek(self):
        return self.elements[- 1]

    def is_empty(self):
        return len(self.elements) == 0
