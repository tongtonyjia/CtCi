class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = StackNode(data)

        if self.top is not None:
            new_node.next = self.top

        self.top = new_node

    def pop(self):
        top = self.top
        if top is not None:
            self.top = self.top.next

        return top

    def peek(self):
        return self.top

    def isEmpty(self):
        return self.top is None
